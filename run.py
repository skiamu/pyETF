# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 19:15:47 2022

@author: skia_
"""
import pandas as pd
import requests
import json
import numpy as np

import requests
import pandas as pd
import funcs
api_url = "https://www.ishares.com/it/investitori-professionali/it/product-screener/product-screener-v3.1.jsn?dcrPath=/templatedata/config/product-screener-v3/data/it/it/product-screener/ishares-product-screener-backend-config&siteEntryPassthrough=true"
response = requests.get(api_url)
resp_dict = response.json()
# df = pd.DataFrame(response.json()).T
# df.columns
for key in resp_dict:
    funcs.parse_etf(resp_dict[key])