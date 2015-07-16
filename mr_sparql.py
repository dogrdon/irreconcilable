#!/usr/bin/env python
from SPARQLWrapper import SPARQLWrapper, JSON
import sys, os
import csv, json, simplejson

input_file = sys.argv[1]

def getSameAs(dbpedia_uri):
	qString = "PREFIX owl: <http://www.w3.org/2002/07/owl#> SELECT * WHERE {<%s> owl:sameAs ?o }" % (dbpedia_uri)
	sparql = SPARQLWrapper("http://dbpedia.org/sparql")
	sparql.setQuery(qString)
	sparql.setReturnFormat(JSON)
	res = sparql.query().convert()
	return res

def getResults(input_file):
	with open(input_file, 'rt') as f:
		reader = csv.reader(f)
		header = reader.next()
		r_counts = 0
		rows = 0
		for row in reader:
			rows += 1
			dbpedia_uri = row[4]
			if dbpedia_uri is not '':
				r_counts += 1
				sameAs = getSameAs(dbpedia_uri)
				for s in sameAs["results"]["bindings"]:
					val = dbpedia_uri, s['o']['value']
					for v in val:
						wkdata = v if 'wikidata' in v else None
					if wkdata is not None:
						print dbpedia_uri, wkdata
		per = float(r_counts)/rows
		print "out of %s records, %s were reconciled: %s" % (rows, r_counts, "{:.1%}".format(per))


if __name__ == '__main__':
	getResults(input_file)



#{ "head": { "link": [], "vars": ["s"] }, "results": { "distinct": false, "ordered": true, "bindings": [ ] } }