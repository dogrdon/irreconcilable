import os, sys
from SPARQLWrapper import SPARQLWrapper, JSON
import urllib
import xml.etree.ElementTree as ET
from pymongo import MongoClient

'''concept here is that you have a list of terms that you want to reconcile with dbpedia
   this uses https://github.com/dbpedia/lookup to generate top scored results
   for a subject term. This is a command line interface that gives you options 
   for selecting the one you think is more accurate to the term you are looking to reconcile'''

_INFILE = sys.argv[1]

#qString = "SELECT * WHERE {?s ?p ?o.}"
#sparql = SPARQLWrapper("http://sparql.freeyourmetadata.org/")
#sparql.addDefaultGraph("http://id.loc.gov/authorities/subjects") #LCSH
#sparql.setQuery(qString)
lookup_uri = 'http://lookup.dbpedia.org/api/search/PrefixSearch?QueryClass=&QueryString=%s'
xmlns = '{http://lookup.dbpedia.org/}%s'


class DBClient(object):
	_client = None
	_collection = None

	def __init__(self):
		self._client = MongoClient()
		self._collection = self._client.ia.subject_terms

	def updateRecord(self, record):
		self._collection.update({'_id':record.keys()[0]}, record, True)

	def updateRecords(self, records):
		for r in records:
			self._collection.update({'_id':r.keys()[0]}, r, True)

	def checkDB(self, term):
		return self._collection.find_one({"_id":term})

def checkresults(results):
	'''show the results to user and have them select one'''
	selection = 'Empty'

	print 'Your term is %s - Choose which one you think is the most accurate from the list below: ' % results['term']
	print 'Select 99 if your answer is not there'

	if results['r_array'] == []:
		print "Sorry, There were not results"
		record = {"NO_RESULTS":raw_input('No Results, suggest an alternative term: ')}
	else:
		for r in results['r_array']:
			print '%s: %s' % (results['r_array'].index(r), r['label'])
		while type(selection) is not int or selection not in range(len(results['r_array'])) and selection != 99:
			try:
				selection = int(raw_input("Enter the number for you choice: ").strip())
			except ValueError:
				print "Not a number, please enter again"
			else:
				print "That's not a valid number for this selection"
		if selection == 99:
			print "Looks like no good results"
			record = {"BAD_RESULTS":raw_input('No Good Results, suggest an alternative term or mark UNKNOWN: ')}
		elif selection != 99:
			record = results['r_array'][selection]
			print "You selected %s, %s" % (selection, record['label'])
	return record

def openterms(f):
	rawterms = open(f, 'rt').readlines() 
	terms = [t.strip() for t in rawterms]
	return terms

def main(db):
	terms = openterms(_INFILE)
	data = []
	for t in terms:
		t = t.encode('utf-8')
		t_query = db.checkDB(t)
		if t_query is None:
			results = {'term':t, 'r_array':[]}
			search_url = lookup_uri % t
			res_xml = urllib.urlopen(search_url).read()
			res_root = ET.fromstring(res_xml)
			res = res_root.findall(xmlns % 'Result')
			for r in res:
				label = r.find(xmlns % 'Label').text
				desc = r.find(xmlns % 'Description').text
				uri = r.find(xmlns % 'URI').text
				results['r_array'].append({'label':label, 'description':desc, 'uri':uri})
			ans = checkresults(results)
			record = {results['term']:ans}
			data.append(record)
			db.updateRecord(record)
	return data


if __name__ == '__main__':
	db = DBClient()
	final = main(db)
	print final