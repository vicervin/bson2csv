""" @author: vicervin
    Python3.5 
    Requires: pandas, pymongo (bson comes from this)
    input: bson file 
    output: csv file with same name
"""

import bson, sys
import pandas as pd
fn = sys.argv[1]
with open(fn,'rb') as f:
    data = bson.decode_all(f.read()) # list of dicts : each row is a dict

fn = fn.replace("bson", "csv")
df = pd.DataFrame(data)
df.to_csv(fn)