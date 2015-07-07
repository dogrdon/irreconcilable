#!/usr/bin/env python
from pymongo import MongoClient
import csv

OUTPUT = "./data/st_results.csv"

c = MongoClient()
coll = c.ia.subject_terms

data = list(coll.find())

def makerow(document):
	k = [x for x in document.keys() if x != '_id']
	term = k[0]
	entry = document[term]
	if 'BAD_RESULTS' in entry:
		row = [term, 'bad results', entry['BAD_RESULTS'], "", "", ""]
	elif 'NO_RESULTS' in entry:
		row = [term, 'no results', entry['NO_RESULTS'], "", "", ""]
	else:
		label = entry['label'] if 'label' in entry else ''
		uri = entry['uri'] if 'uri' in entry else ''
		desc = entry['description'] if 'description' in entry else ''
		if desc is not None:
			desc = desc.encode('utf8').strip()
		row = [term, 'success', "", label.encode('utf8'), uri.encode('utf8'), desc]
	return row

with open(OUTPUT, 'w') as f:
	w = csv.writer(f)
	head = ["term", "r_status", "reason or alt", "label", "uri", "description"]
	w.writerow(head)
	for d in data:
		row = makerow(d)
		w.writerow(row)



