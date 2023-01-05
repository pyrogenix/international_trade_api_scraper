import requests
import pandas as pd
import os

API_KEY = '0c63e782330f5e58626e87dc01cc7eb2174680c5'

# TIME = '2020-01'

EXPORT_COLS_HS = [
    'YEAR',
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

EXPORT_COLS_PORTHS = [
    'YEAR',
    'MONTH',
    'PORT',
    'PORT_NAME',
    'CTY_CODE',
    'E_COMMODITY',
]

def cols_to_str(COLS):
    return ','.join(i for i in COLS)

# EXPORT_URL = f'https://api.census.gov/data/timeseries/intltrade/exports/hs?get={EX_COL_STR}&key={API_KEY}&time={TIME}'

def json_to_df(response):
    return pd.DataFrame(response.json()[1:], columns=response.json()[0])

def scrape_range(year,month):
    while year < 2021:
        m = "{:02d}".format(month)
        scrape(f'{year}-{m}')
        month += 1
        if month == 13:
            month=1
            year += 1

def scrape(TIME, ENDPOINT):
    if endpoint == "hs":
        EX_COL_STR = cols_to_str(EXPORT_COLS_HS)
    elif endpoint == "porths":
        EX_COL_STR = cols_to_str(EXPORT_COLS_PORTHS)
    else:
        print("Invalid endpoint, terminating program.")
        exit()
    EXPORT_URL = f'https://api.census.gov/data/timeseries/intltrade/exports/{ENDPOINT}?get={EX_COL_STR}&key={API_KEY}&time={TIME}'
    response = requests.request("GET", EXPORT_URL)
    df = json_to_df(response)
    response.close()
    os.makedirs('./output/export', exist_ok=True)  
    df.to_csv(f'./output/export/EXPORT_{TIME}.csv', index=False)

def main():
    endpoint = input("What endpoint would you like to scrape? (hs or porths)")
    date = input('What date would you like to scrap values from? (format YYYY-MM)')
    scrape(date, endpoint)


main()