import time
from datetime import datetime, timedelta
import requests
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
    sd = stringdate_to_datetime(string_startdate)
    ed = stringdate_to_datetime(string_enddate)
    delta = timedelta(hours=1)
    while sd <= ed:
        print(generate_bitcoin_url(sd, sd+delta))
        sd += delta


x = '2017-12-01 00:00:00'
y = '2017-12-08 13:00:00'
print(get_crypto_historical_data(x, y))


# input start_date and end_date, automatically adds time(00:00:00)
# for loop that increases one hour (timedelta(hours=1))
# generate csv of all the urls to loop through based on start_date
# and end_date hourly intervals
# loop to get data from each hour between start_date and end_date

# r = requests.get(url)
# print(r.headers)
