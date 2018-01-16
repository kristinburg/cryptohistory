import time
from datetime import datetime, timedelta
import requests
import json
import csv
from date_utils import (
    datetime_to_timestamp, stringdate_to_datetime,
    stringdate_to_string_datetime, validate_date_string
)


def generate_bitcoin_url(start_datetime_obj, end_datetime_obj):
    start_timestamp = datetime_to_timestamp(start_datetime_obj)
    end_timestamp = datetime_to_timestamp(end_datetime_obj)
    url = 'https://graphs.coinmarketcap.com/currencies/bitcoin'
    return f'{url}/{start_timestamp}/{end_timestamp}/'


def generate_ethereum_url(start_datetime_obj, end_datetime_obj):
    start_timestamp = datetime_to_timestamp(start_datetime_obj)
    end_timestamp = datetime_to_timestamp(end_datetime_obj)
    url = 'https://graphs.coinmarketcap.com/currencies/ethereum'
    return f'{url}/{start_timestamp}/{end_timestamp}/'


def response_to_csv_rows(json_response):
    # takes json_response and returns csv rows
    market_caps = json_response['market_cap_by_available_supply']
    price_btcs = json_response['price_btc']
    price_usds = json_response['price_usd']
    volume_usds = json_response['volume_usd']
    csv_rows = []

    for i, market_cap in enumerate(market_caps):
        timestamp = market_cap[0]
        market_cap_value = market_cap[1]
        price_btc_value = price_btcs[i][1]
        price_usd_value = price_usds[i][1]
        volume_usd_value = volume_usds[i][1]
        csv_row = [timestamp, market_cap_value, price_btc_value,
                   price_usd_value, volume_usd_value]
        csv_rows.append(csv_row)
    return csv_rows


def get_crypto_historical_data(string_startdate, string_enddate):
    with open('output.csv', 'w', 1) as output:
        csv_headers = ['timestamp','market_cap','price_btc','price_usd', 'volume']
        writer = csv.writer(output)
        writer.writerow([g for g in csv_headers])

        sd = stringdate_to_datetime(string_startdate)
        ed = stringdate_to_datetime(string_enddate)
        delta = timedelta(hours=1)
        url = generate_bitcoin_url(sd, sd+delta)

        while sd <= ed:
            response = requests.get(url)
            data = response.json()
            csv_row = response_to_csv_rows(data)
            output.write(csv_row + '\n')
            sd += delta
        output.close()


if __name__ == '__main__':
    """
    Only run this code when explicitly calling it. (not via import)
    """
    x = '2017-12-01 00:00:00'
    y = '2017-12-01 2:00:00'

    get_crypto_historical_data(x, y)
    # r = requests.get(url)
    # print(r.headers)
