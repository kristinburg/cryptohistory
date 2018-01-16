import csv
from datetime import timedelta

import requests

from date_utils import (
    datetime_to_timestamp, stringdate_to_datetime,
    stringdate_to_string_datetime
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


def get_crypto_historical_data_by_string(string_startdate, string_enddate,
                                         delta=timedelta(days=1)):
    string_startdatetime, string_enddatetime = (
        stringdate_to_string_datetime(string_startdate),
        stringdate_to_string_datetime(string_enddate, end=True)
    )

    start_date = stringdate_to_datetime(string_startdatetime)
    end_date = stringdate_to_datetime(string_enddatetime)

    # startdate should be earlier than enddate
    if start_date > end_date:
        raise ValueError('Start date can\t be later than end date.')

    get_crypto_historical_data(start_date, end_date, delta)


def get_crypto_historical_data(start_date, end_date, delta=timedelta(days=1)):

    with open('output.csv', 'w', 1) as output:
        csv_headers = [
            'timestamp', 'market_cap', 'price_btc', 'price_usd', 'volume']
        writer = csv.writer(output)
        writer.writerow([csv_header for csv_header in csv_headers])

        url = generate_bitcoin_url(start_date, end_date + delta)

        while start_date <= end_date:
            response = requests.get(url)
            data = response.json()
            csv_rows = response_to_csv_rows(data)
            for csv_row in csv_rows:
                output.write(','.join([str(x) for x in csv_row]) + '\n')
            start_date += delta


if __name__ == '__main__':
    """
    Only run this code when explicitly calling it. (not via import)
    """
    start_date = '2017-12-01'
    end_date = '2017-12-02'

    get_crypto_historical_data_by_string(start_date, end_date)
