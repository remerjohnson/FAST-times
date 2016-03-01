# FAST Times

### Description

`FAST_times.py` is a script that takes existing LCSH subjects from the DAMS along with their ID/URI (in this case, an ARK) and spits those into .csv files.  

It also formats the subjects in order to effectively query them against the [FAST API](https://experimental.worldcat.org/fast/).  

The FAST API returns suggestions, which contain the authorized heading, its ID, and the MARC tag number. The script puts that into a third .csv file.  

`concatenate.py` is a script that then concatenates the three .csv files (using the Python library [pandas](http://pandas.pydata.org/pandas-docs/stable/)) into one master spreadsheet.  

This spreadsheet can then be imported to OpenRefine for data munging. In this case, it's used to parse the JSON responses from the API, create rows based on the number of responses, parse the IDs into valid URLs, and display the relevant MARC tag.  

# Less FAST Times

In not-so-fast times, we need a different solution. `less_FAST_times.py` strips out the API calling of the original script, and instead relies on an existing [OpenRefine reconciliation script](https://github.com/cmh2166/fast-reconcile) (credit to [Christina Harlow](https://github.com/cmh2166)).  

# Reference to other scripts

Once in OpenRefine, a separate script uses OpenRefine's own reconciliation functionality to generate a reconciliation service. My slight tweak to the original script is that instead of a ranked number being returned reflecting the match accuracy of the term, it instead returns the MARC tag number that the subject/genre falls under. You can see my tweak/fork [here](https://github.com/remerjohnson/fast-reconcile).   
