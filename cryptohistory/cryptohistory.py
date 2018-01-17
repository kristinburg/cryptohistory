import csv
import time
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
    url = 'https://graphs2.coinmarketcap.com/currencies'
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


def generate_currency_api_urls(start_datetime,
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

    start_datetime = stringdate_to_datetime(string_startdatetime)
    end_datetime = stringdate_to_datetime(string_enddatetime)

    # startdate should be earlier than enddate
    if start_datetime > end_datetime:
        raise ValueError('Start date can\t be later than end date.')

    # validate that a correct currency is being used
    validate_currency(currency)

    _get_crypto_historical_data(
        start_datetime, end_datetime, delta=delta, currency=currency)


def _get_crypto_historical_data(start_datetime,
                                end_datetime,
                                delta=timedelta(days=1),
                                currency=BTC):
    csv_headers = [
        'timestamp', 'market_cap', 'price_btc', 'price_usd', 'volume']

    filename = f'{currency}-{start_datetime}-{end_datetime}.csv'

    with open(filename, 'w', 1) as output:
        writer = csv.writer(output)
        writer.writerow([csv_header for csv_header in csv_headers])

        generated_urls = generate_currency_api_urls(
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            delta=delta,
            currency=currency)

        def try_response(url, attempt=0):
            response = requests.get(url)
            if response.status_code == 200:
                csv_rows = response_to_csv_rows(response.json())

                for csv_row in csv_rows:
                    output.write(','.join([str(x) for x in csv_row]) + '\n')
            else:
                time.sleep(2 + attempt)
                try_response(url=url, attempt=(attempt * 2))
                if attempt > 64:
                    raise ValueError(
                        'Tried too many times for url: {url}'.format(url))

        for url in generated_urls:
            try_response(url)


if __name__ == '__main__':
    """
    Only run this code when explicitly calling it. (not via import)
    """
    start_date = '2017-10-25'
    end_date = '2018-01-16'
    currency = BTC
    delta = timedelta(days=1)

    get_crypto_historical_data(start_date, end_date, delta, currency)
