import requests
import pandas as pd
import os

API_KEY = '0c63e782330f5e58626e87dc01cc7eb2174680c5'

TIME = '2020-01'

EXPORT_COLS = [
    'MONTH',
    'CTY_CODE',
    'CTY_NAME',
    'QTY_1_MO',
    'E_COMMODITY',
    'UNIT_QY1',
    'ALL_VAL_MO',
    'DISTRICT',
    'DIST_NAME'
]

def cols_to_str(COLS):
    return ','.join(i for i in COLS)

EX_COL_STR = cols_to_str(EXPORT_COLS)

EXPORT_URL = f'https://api.census.gov/data/timeseries/intltrade/exports/hs?get={EX_COL_STR}&key={API_KEY}&time={TIME}'

def json_to_df(response):
    return pd.DataFrame(response.json()[1:], columns=response.json()[0])

def main():
    response = requests.request("GET", EXPORT_URL)
    df = json_to_df(response)
    response.close()
    os.makedirs('./output', exist_ok=True)  
    df.to_csv(f'./output/EXPORT_{TIME}.csv', index=False)
    

main()