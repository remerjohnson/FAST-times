# -*- coding: utf-8 -*-

import json
from pprint import pprint
from operator import itemgetter
import requests
import csv
import re
from itertools import chain
from itertools import izip
import codecs
import unicodedata 

# some config
api_base_url = "http://fast.oclc.org/searchfast/fastsuggest"
#For constructing links to FAST.
fast_uri_base = "http://id.worldcat.org/fast/{0}"

# Open the file we're provided. The Python library 'requests' recommends opening as read and binary, 'rb' 
f1 = codecs.open("topic.tsv", "rb", "utf-8")

# Set up to write to .csv files
f2 = csv.writer(open('arks.csv', 'w'))
f3 = csv.writer(open('dams_subjects.csv', 'w'))
f4 = csv.writer(open('output.csv', 'w'))


# Create empty ARK list we can append all the ARKs from the input file to:
arks = []
# Create empty subjects list we can append all the raw DAMS subjects from the input file to:
dams_subjects = []
# Create empty subjects list we can append all the 'cleaned up' DAMS subjects to:
subjects = []
# Set up loop to isolate ARKs and subjects from each line in the spreadsheet, add to lists:
for line in f1:
	# FAST API can't handle multiple spaces OR hyphens. 
	# Need a lot of re.sub here to catch extra spaces and hyphen combinations
	dams_subj = re.findall("\t(.+)\t", line, flags=re.UNICODE)
	dams_subjects.append(dams_subj)
	line = re.sub(r"\?", r"", line, flags=re.UNICODE)
	line = re.sub(r"\(", r"", line, flags=re.UNICODE)
	line = re.sub(r"\)", r"", line, flags=re.UNICODE)
	line = re.sub(r",", r"", line, flags=re.UNICODE)
	line = re.sub(r"\[", r"", line, flags=re.UNICODE)
	line = re.sub(r"\]", r"", line, flags=re.UNICODE)
	line = re.sub(r" -- ", r" ", line, flags=re.UNICODE)
	line = re.sub(r" --", r" ", line, flags=re.UNICODE)
	line = re.sub(r"-- ", r" ", line, flags=re.UNICODE)
	line = re.sub(r"--", r" ", line, flags=re.UNICODE)
	line = re.sub(r"  ", r" ", line, flags=re.UNICODE)
	ark = re.findall("^(http.+?)\t", line, flags=re.UNICODE)
	arks.append(ark)
	subj = re.findall("\t(.+)\t", line, flags=re.UNICODE)
	subjects.append(subj)
	continue

# Format the ARKs and DAMS subjects better as a list:
final_arks = list(chain(*arks))
final_dams = list(chain(*dams_subjects))

# Write out the ARKs into a single column csv:
for a in final_arks:
	f2.writerow([a])

# Write out the DAMS subject labels as they appear in the DAMS to a single column csv:
for s in final_dams:
	f3.writerow([s.encode('UTF-8')])

# Format the cleaned up subjects better to get a good API response:
final_subjects = list(chain(*subjects))

# Set up a loop for 'requests' to take each subject and run it against the FAST API, write the result to csv:
for i in final_subjects:
	url = api_base_url + '?&query=' + unicode(i)
	url += '&queryIndex=suggestall&queryReturn=suggestall,idroot,auth,tag,raw&suggest=autoSubject&rows=3&wt=json'
	r = requests.get(url)
	r.encoding = 'utf-8'
	f4.writerow([r.text.encode('UTF-8')])
	continue


# Get back the header info for the FAST server/API
print r.headers
print r.encoding
print r.text