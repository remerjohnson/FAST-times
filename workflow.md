+ Get the `topic.txt` list of topics from JIRA
+ Convert to csv: `topic.txt > topic.csv`
+ Cut columns we don't need via `csvkit`'s `csvcut`:  ```csvcut -t -c ark,topic topic.csv > new_topic.csv```
+ Convert to tsv: `cat new_topic.csv | sed 's/,/\t/g' > topic.tsv`
+ Run script that creates all the csv files: `python less_FAST_times.py`
+ Run the concatenate script: `python concatenate.py`
+ Open result `concatenated.csv` in OpenRefine
+ Check for any obvious anomalies via faceting, clusters
+ Run reconciliation service for FAST by `cd` into the `fast-reconcile` repo and run: `python reconcile.py`
+ Select options on clean_labels column, then select reconcile: follow prompts
+ Review matches. When satisfied, extract label, URI, marc tag into new columns
+ Export to Excel
