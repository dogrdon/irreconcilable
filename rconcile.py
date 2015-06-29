import os, sys
from SPARQLWrapper import SPARQLWrapper, JSON
import urllib
import xml.etree.ElementTree as ET

'''concept here is that you have a list of terms that you want to reconcile with dbpedia
   this uses https://github.com/dbpedia/lookup to get generate top scored results
   for a subject term. This is a command line interface that gives you options 
   for selecting the one you think is more accurate to the term you are looking to reconcile'''

_INFILE = sys.argv[1]

qString = "SELECT * WHERE {?s ?p ?o.}"
sparql = SPARQLWrapper("http://sparql.freeyourmetadata.org/")
sparql.addDefaultGraph("http://id.loc.gov/authorities/subjects") #LCSH
sparql.setQuery(qString)
lookup_uri = 'http://lookup.dbpedia.org/api/search/PrefixSearch?QueryClass=&QueryString=%s'
xmlns = '{http://lookup.dbpedia.org/}%s'

def checkresults(results):
	'''show the results to user and have them select one'''
	for r in results['r_array']:
		print 'choose which one is correct'
		'''all the logic for choosing which one and returne the right one'''


def openterms(f):
	rawterms = open(f, 'rt').readlines() 
	terms = [t.strip() for t in rawterms]
	return terms

def main():
	terms = openterms(_INFILE)
	data = {}
	for t in terms:
		results = {'term':t, r_array:[]}
		search_url = lookup_uri % t
		res_xml = urllib.openurl(search_url)
		res_root = ET.fromstring(res_xml)
		res = res_root.findall(xmlns % 'Result')
		for r in res:
			label = r.find(xmlns % 'Label')
			desc = r.find(xmlns % 'Description')
			uri = r.find(xmlns % 'URI')
			results.r_array.append({'label':label, 'description':desc, 'uri':uri})
		ans = checkresults(results)
		data['term'] = ans
	'''more magic here'''
	return data




if __name__ == '__main__':
	final = main()
	print final