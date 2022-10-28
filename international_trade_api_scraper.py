import requests
import pandas as pd

API_KEY = '0c63e782330f5e58626e87dc01cc7eb2174680c5'

TIME = '2020-01'

EXPORT_URL = f'https://api.census.gov/data/timeseries/intltrade/exports/hs?get=MONTH,CTY_CODE,CTY_NAME,QTY_1_MO,E_COMMODITY,UNIT_QY1,ALL_VAL_MO&key={API_KEY}&time={TIME}'

# print(response.text)

def json_to_df(response):
    return pd.DataFrame(response.json()[1:], columns=response.json()[0])

def main():
    response = requests.request("GET", EXPORT_URL)
    df = json_to_df(response)
    response.close()
    print(df)

main()