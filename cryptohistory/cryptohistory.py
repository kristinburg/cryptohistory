import time
from datetime import datetime, timedelta
import requests
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


def get_crypto_historical_data(string_startdate, string_enddate):
    with open('output.csv', 'w', 1) as output:
        sd = stringdate_to_datetime(string_startdate)
        ed = stringdate_to_datetime(string_enddate)
        delta = timedelta(hours=1)
        url = (generate_bitcoin_url(sd, sd+delta))
        r = requests.get(url)
        while sd <= ed:
            output.write(url + '\n')
            print(r.text)
            sd += delta
        output.close()

x = '2017-12-01 00:00:00'
y = '2017-12-01 6:00:00'
print(get_crypto_historical_data(x, y))

# r = requests.get(url)
# print(r.headers)
