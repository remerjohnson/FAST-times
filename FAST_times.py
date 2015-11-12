#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from operator import itemgetter
import urllib
import requests
import csv
import re

#some config
api_base_url = 'http://fast.oclc.org/searchfast/fastsuggest'
#For constructing links to FAST.
fast_uri_base = 'http://id.worldcat.org/fast/{0}'

# Open the file. Python library Requests recommends opening as read and binary, 'rb' 
f1 = open('geographic.csv', 'rb')

# Set up to write to a csv file, write coulmn headers
# f2 = 

# Create empty subjects list we can append all the subjects from column B to:
subjects = []
for line in f1:
	# FAST API can't handle spaces or hyphens. 
	# Need a lot of re.sub here to catch spaces and -- combinations
	line = re.sub(r" -- ", r"%20", line)
	line = re.sub(r" --", r"%20", line)
	line = re.sub(r"-- ", r"%20", line)
	line = re.sub(r"--", r"%20", line)
	line = re.sub(r" ", r"%20", line)
	subj = re.findall("\t(.+)\t", line, flags=re.UNICODE)
	subjects.append(subj)
	continue

# Get the list without quotes?

# Uncomment the following statement if you want to return the full subject list
# in your terminal output:
# print json.dumps(subjects, ensure_ascii=False)
results = []

for i in subjects:
	url = api_base_url + '?&query=' + str(i).encode('UTF-8') 
	url += '&queryIndex=suggestall&queryReturn=suggestall%2Cidroot%2Cauth%2Ctag%2Craw&suggest=autoSubject&rows=13&wt=json'
	r = requests.get(url)
	results.append(r.text)
	continue

print r.headers
print results