import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
import re


def parse_etf(etf_dict):
    # logging.info()
    for key, value in etf_dict.items():
         if isinstance(value, dict) and ('r' in value and 'd' in value):
             etf_dict[key] = etf_dict[key]['r']
         elif isinstance(value, str):
             etf_dict[key] = etf_dict[key].strip('[]')