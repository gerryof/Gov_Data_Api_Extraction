# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 10:50:37 2021

@author: Data
"""
import pandas as pd
import jsonstat
import os


url = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/CJA07/JSON-stat/2.0/en'

filename = "crimeapi.json"

# A correction was needed in the jsonstat package, in download.py on line 58. 
# html = response.text needed to be changed to
# html = response.text.encode('cp850','replace').decode('cp850')
cache = jsonstat.download(url, filename)

pathname = os.path.join(r"C:\Users\Data\data" , filename)

data = jsonstat.from_file(pathname)

df = data.to_data_frame()


