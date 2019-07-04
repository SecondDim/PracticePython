#! /usr/local/bin/python3

# pip3 install --upgrade gspread ServiceAccountCredentials
# pip3 install --upgrade PyOpenSSL
# pip3 install python-binance

# gspread https://github.com/burnash/gspread
# Other way use https://github.com/david-pettifor-nd/easy-google-docs

# binance https://github.com/binance-exchange/python-binance
# bitopro https://developer.bitopro.com/docs

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
import os
import json
import requests

from binance.client import Client

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://spreadsheets.google.com/feeds',
          'https://www.googleapis.com/auth/drive']

# The spreadsheet ID
SPREADSHEET_ID = '1Dt1YuO_wLH_DeHu8uh6FYtvzvLWN5jIPIs7SPPprxPQ'

# Trace market
MARKETS_SYMBOL = ['BTCUSDT', 'ETHUSDT', 'LTCUSDT', 'BNBUSDT',
                  'XMRUSDT', 'KNCETH', 'TUSDUSDT']


def update_sheet(service, spreadsheet_id, update_data):
    worksheet = service.open_by_key(spreadsheet_id).sheet1

    for index, value in enumerate(update_data):
        worksheet.update_acell('A%s' % (index+3), value['symbol'])
        worksheet.update_acell('B%s' % (index+3), value['price'])

    update_at = time.strftime("%Y-%m-%d %H:%M:%S")
    worksheet.update_acell('B1', update_at)

    print('Last update_at: %s' % update_at, end='\r')


def binance_client(binance_api_key='ENV/binance-api-key.json'):
    if not os.path.exists(binance_api_key):
        raise "%s file is not exists." % binance_api_key

    with open(binance_api_key) as f:
        binance = json.load(f)

    return Client(binance['api_key'], binance['api_secret'])


def bitopro_open_api(request_method=None, request_params=None, request_url='https://api.bitopro.com/v2'):
    if request_method == None or request_params == None:
        raise "Missing args. func <<bitopro_open_api>>"

    request_url = "%s/%s/%s" % (request_url, request_method, request_params)
    r = requests.get(request_url)

    if not r.ok:
        raise "Api request fail. func <<bitopro_open_api>>"

    return r.json()


def gspread_service(service_account_key='ENV/service-account-key.json'):

    if not os.path.exists(service_account_key):
        raise "%s file is not exists." % service_account_key

    service_account = ServiceAccountCredentials.from_json_keyfile_name(
        service_account_key, SCOPES)

    return gspread.authorize(service_account)


def main():
    service = gspread_service()

    update_data = []

    # Binance
    client = binance_client()
    all_tickers = client.get_all_tickers()
    for ticker in all_tickers:
        if ticker['symbol'] in MARKETS_SYMBOL:
            update_data.append(ticker)

    # Bitopro
    bitopro_response = bitopro_open_api(
        request_method='tickers', request_params='btc_twd')
    update_data.append({'symbol': 'BTCTWD',
                        'price': bitopro_response['data']['lastPrice']})

    bitopro_response = bitopro_open_api(
        request_method='tickers', request_params='eth_twd')
    update_data.append({'symbol': 'ETHTWD',
                        'price': bitopro_response['data']['lastPrice']})

    bitopro_response = bitopro_open_api(
        request_method='tickers', request_params='usdt_twd')
    update_data.append({'symbol': 'USDTTWD',
                        'price': bitopro_response['data']['lastPrice']})

    update_sheet(service, SPREADSHEET_ID, update_data)


if __name__ == '__main__':
    while True:
        main()
        time.sleep(60)
