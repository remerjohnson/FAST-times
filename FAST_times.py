# -*- coding: utf-8 -*-

import json
from operator import itemgetter
import urllib
import requests
import csv
import re
from itertools import chain
import codecs
import unicodedata 

#some config
api_base_url = "http://fast.oclc.org/searchfast/fastsuggest"
#For constructing links to FAST.
fast_uri_base = "http://id.worldcat.org/fast/{0}"

# Open the file. The Python library Requests recommends opening as read and binary, 'rb' 
f1 = codecs.open("geographic.csv", "rb", "utf-8")

# Set up to write to a csv file, and write coulmn headers
# f2 = 

# Create empty subjects list we can append all the subjects from column B to:
subjects = []
for line in f1:
	# FAST API can't handle spaces or hyphens. 
	# Need a lot of re.sub here to catch spaces and -- combinations
	line = re.sub(r" -- ", r" ", line, flags=re.UNICODE)
	line = re.sub(r" --", r" ", line, flags=re.UNICODE)
	line = re.sub(r"-- ", r" ", line, flags=re.UNICODE)
	line = re.sub(r"--", r" ", line, flags=re.UNICODE)
	line = re.sub(r"  ", r" ", line, flags=re.UNICODE)
	subj = re.findall("\t(.+)\t", line, flags=re.UNICODE)
	subjects.append(subj)
	continue




# Uncomment the following statement(s) if you want to return the full subject list
# in your terminal output:
# final_subjects = json.dumps(subjects, ensure_ascii=False)

# print json.dumps(subjects, ensure_ascii=False)
final_subjects = list(chain(*subjects))
#final_subjects = json.dumps(final_subjects, ensure_ascii=False)
print final_subjects
# print subjects 
results = []

for i in final_subjects:
	url = api_base_url + '?&query=' + unicode(i)
	url += '&queryIndex=suggestall&queryReturn=suggestall,idroot,auth,tag,raw&suggest=autoSubject&rows=3&callback=test02'
	r = requests.get(url)
	results.append(r.text)
	continue


# Sample query to see how Requests works:
#url = "http://fast.oclc.org/searchfast/fastsuggest?&query=Madrid%20Madrid%20Spain&queryIndex=suggestall&queryReturn=suggestall,idroot,auth,tag,raw&suggest=autoSubject&rows=3&callback=test02"
#r = requests.get(url)

# Get back the header info for the FAST server/API
#print r.headers
#print results

final_results = json.dumps(results, sort_keys = True, indent=4, ensure_ascii=False)
print final_results

# Isolate the auth label and FAST URIs so we can put them in the spreadsheet
#for line in final_results:


#Print a file with the json data for each subject on a line
#with codecs.open('data.json', 'w', 'utf8') as f2:
#     f2.write(json.dumps(results, sort_keys = True, indent=4, ensure_ascii=False))

#f1.close()
#f2.close()