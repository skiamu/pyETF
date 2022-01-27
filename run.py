# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 19:15:47 2022

@author: skia_
"""
import pandas as pd
import requests
import json
import numpy as np

out = requests.get(url = "https://www.ishares.com/it/investitori-professionali/it/product-screener/product-screener-v3.jsn?dcrPath=/templatedata/config/product-screener-v3/data/it/it/product-screener/product-screener&siteEntryPassthrough=true")
print(out.status_code)
print(out.json())
print(json.dumps(out.json(), indent=4, sort_keys=True))
out.content
json_raw = out.json()
columns_dict = json_raw['data']['tableData']['columns']
columns_list = [x['name'] for x in json_raw['data']['tableData']['columns']]
data_list = json_raw['data']['tableData']['data']
data_list_2 = [None] * len(data_list)
for i in range(len(data_list)):
    data_list_2[i] = [x['r'] if type(x) is dict else x for x in data_list[i]]

df = pd.DataFrame(data=data_list_2, columns=columns_list)
df = df.replace('-', np.NaN)
data_list_2 = [x['r'] if type(x) is dict else x for x in data_list]
df = pd.DataFrame(data_list)
