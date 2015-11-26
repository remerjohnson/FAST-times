# -*- coding: utf-8 -*-

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

#some config
api_base_url = "http://fast.oclc.org/searchfast/fastsuggest"
#For constructing links to FAST.
fast_uri_base = "http://id.worldcat.org/fast/{0}"

# Open the file. The Python library Requests recommends opening as read and binary, 'rb' 
f1 = codecs.open("geographic.csv", "rb", "utf-8")

# Set up to write to a csv file, and write coulmn headers
f2 = csv.writer(open('output.csv', 'w'))



# Create empty ARK list we can append all the ARKs from column A to:
arks = []
# Create empty subjects list we can append all the subjects from column B to:
subjects = []
# Set up loop to isolate ARKs and subjects from each line in the spreadsheet, add to lists:
for line in f1:
	# FAST API can't handle multiple spaces OR hyphens. 
	# Need a lot of re.sub here to catch extra spaces and hyphen combinations
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




# Uncomment the following statement(s) if you want to return the full subject list
# in your terminal output:
# final_subjects = json.dumps(subjects, ensure_ascii=False)
print arks
# print json.dumps(subjects, ensure_ascii=False)
final_subjects = list(chain(*subjects))
#final_subjects = json.dumps(final_subjects, ensure_ascii=False)
print final_subjects
# print subjects 
results = []


# f2.write(json.dumps(results, sort_keys = True, indent=4, ensure_ascii=False))
for i in final_subjects:
	url = api_base_url + '?&query=' + unicode(i)
	url += '&queryIndex=suggestall&queryReturn=suggestall,idroot,auth,tag,raw&suggest=autoSubject&rows=3&wt=json'
	r = requests.get(url)
	f2.writerow([r.text.encode('UTF-8')])
	continue


# Get back the header info for the FAST server/API
print r.headers
print r.encoding
print r.text
#pprint(results)

final_results = []

#for line in results:
#	l1 = line.split()
#	final_results.append(l1)
#	continue


#cool_results = json.dumps(final_results, indent=4, ensure_ascii=False)
#print cool_results


auths = []
# Isolate the auth label and FAST URIs so we can put them in the spreadsheet

#auth = re.findall(r'auth\\":\\"(.+),', final_results, flags=re.UNICODE | re.MULTILINE)
#for a in auth:
#	auths.append(a)
#	continue

#print auths 



#Print a file with the json data for each subject on a line
#with codecs.open('data.json', 'w', 'utf8') as f2:
#     f2.write(json.dumps(results, sort_keys = True, indent=4, ensure_ascii=False))

#with open("data.json") as json_file:
#        json_data = json.load(json_file)
 #       print(json_data)

#f1.close()
#f2.close()