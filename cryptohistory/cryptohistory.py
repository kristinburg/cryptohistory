import csv
from datetime import timedelta

import requests

from date_utils import (
    datetime_to_timestamp, stringdate_to_datetime,
    stringdate_to_string_datetime
)

BTC = 'bitcoin'
ETH = 'ethereum'

AVAILABLE_CURRENCIES = [
    BTC, ETH
]


def validate_currency(value):
    if value not in AVAILABLE_CURRENCIES:
        raise ValueError(f'{value} is not a valid currency')


def generate_currency_url(start_datetime, end_datetime, currency=BTC):
    validate_currency(currency)

    start_timestamp = datetime_to_timestamp(start_datetime)
    end_timestamp = datetime_to_timestamp(end_datetime)
    url = 'https://graphs.coinmarketcap.com/currencies'
    return f'{url}/{currency}/{start_timestamp}/{end_timestamp}/'


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


def generate_api_urls(start_datetime,
                      end_datetime,
                      currency=BTC,
                      delta=timedelta(days=1)):
    """
    Return a list of generated urls for given start_date, end_date, delta &
    currency.

    :param start_date DateTime
    :param end_date DateTime

    :return: list of API urls
    :rtype: list of str
    """
    previous_datetime = start_datetime
    next_datetime = start_datetime + delta

    urls = []

    while previous_datetime <= end_datetime:
        urls.append(
            generate_currency_url(
                previous_datetime, next_datetime, currency=currency))

        # now increase them
        previous_datetime += delta
        next_datetime += delta

    return urls


def get_crypto_historical_data(string_startdate,
                               string_enddate,
                               delta=timedelta(days=1),
                               currency=BTC):

    string_startdatetime, string_enddatetime = (
        stringdate_to_string_datetime(string_startdate),
        stringdate_to_string_datetime(string_enddate, end=True)
    )

    start_date = stringdate_to_datetime(string_startdatetime)
    end_date = stringdate_to_datetime(string_enddatetime)

    # startdate should be earlier than enddate
    if start_date > end_date:
        raise ValueError('Start date can\t be later than end date.')

    # validate that a correct currency is being used
    validate_currency(currency)

    _get_crypto_historical_data(start_date, end_date, delta)


def _get_crypto_historical_data(start_date,
                                end_date,
                                delta=timedelta(days=1),
                                currency=BTC):

    with open('output.csv', 'w', 1) as output:
        csv_headers = [
            'timestamp', 'market_cap', 'price_btc', 'price_usd', 'volume']
        writer = csv.writer(output)
        writer.writerow([csv_header for csv_header in csv_headers])

        url = generate_currency_url(start_date, end_date + delta)

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
    currency = BTC
    delta = timedelta(days=1)

    get_crypto_historical_data(start_date, end_date, delta, currency)
