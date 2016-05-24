# coding: utf-8

import json
from pprint import pprint
from operator import itemgetter
import urllib
import requests
import csv
import re
from itertools import chain
import codecs
import unicodedata

# some config
api_base_url = "http://fast.oclc.org/searchfast/fastsuggest"
#For constructing links to FAST.
fast_uri_base = "http://id.worldcat.org/fast/{0}"

# Open the file we're provided. The Python library 'requests' recommends opening as read and binary, 'rb'
f1 = open('topic.tsv', 'r')

# Set up to write to .csv files
f2 = csv.writer(open('arks.csv', 'w'))
f3 = csv.writer(open('dams_subjects.csv', 'w'))
f4 = csv.writer(open('clean_labels.csv', 'w'))


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
	line = re.sub(r"\[", r"", line, flags=re.UNICODE)
	line = re.sub(r"\]", r"", line, flags=re.UNICODE)
	line = re.sub(r" -- ", r"--", line, flags=re.UNICODE)
	line = re.sub(r" --", r"--", line, flags=re.UNICODE)
	line = re.sub(r"-- ", r"--", line, flags=re.UNICODE)
	line = re.sub(r"---", r"--", line, flags=re.UNICODE)
	line = re.sub(r"  ", r" ", line, flags=re.UNICODE)
	ark = re.findall("^(http.+?)\t", line, flags=re.UNICODE)
	arks.append(ark)
	subj = re.findall("\t(.+)\t", line, flags=re.UNICODE)
	subjects.append(subj)
	continue

# Format the ARKs and DAMS subjects better as a list:
final_arks = list(chain(*arks))
final_dams = list(chain(*dams_subjects))
final_subjects = list(chain(*subjects))

# Write out the ARKs into a single column csv:
for a in final_arks:
	f2.writerow([a])

# Write out the DAMS subject labels as they appear in the DAMS to a single column csv:
for s in final_dams:
	f3.writerow([s])

# Write out the 'cleaned up' DAMS subject labels to a single column csv:
for i in final_subjects:
	f4.writerow([i])

# Print final lists to the terminal to see any obvious errors:
print (final_arks)
print (final_dams)
print (final_subjects)
