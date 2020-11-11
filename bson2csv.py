""" @author: vicervin
    @authorUpdate: igle 
    Python3.5 
    Requires: pandas, pymongo (bson comes from this)
    input: bson file 
    output: csv file with same name
"""

import bson, sys
import pandas as pd
import os

files=sorted(list(os.walk('./bson/.'))[0][2])
print(files)

bsons=[x for x in files if '.bson' == x[-5:].lower()]

for file in enumerate(bsons):
    fn = file[1]
    print(fn)
    with open('bson/'+fn,'rb') as f:
        data = bson.decode_all(f.read()) # list of dicts : each row is a dict

    fn = fn.replace("bson", "csv")
    df = pd.DataFrame(data)
    df.to_csv("csv/"+fn)

