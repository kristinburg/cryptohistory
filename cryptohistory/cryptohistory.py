import time
from datetime import datetime
import requests


# append H:M:S to datetime
def stringdate_to_stringdatetime(string_date, end=False):
    validate_date_string(string_date)
    if end:
        return '{0} 23:59:59'.format(string_date)
    return '{0} 00:00:00'.format(string_date)


def validate_date_string(value):
    try:
        datetime.strptime(value, '%Y-%m-%d')
    except ValueError:
        raise ValueError('Incorrect data format, should be YYYY-MM-DD')


# convert string_date to datetime object
def stringdate_to_datetime(string_datetime):
    return datetime.strptime(string_datetime, '%Y-%m-%d %H:%M:%S')


# convert string date to integer in milliseconds (for url)
def datetime_to_timestamp(dt):
    return int(dt.timestamp()) * 1000


def generate_bitcoin_url(start_datetime, end_datetime):
    start_timestamp = datetime_to_timestamp(timestamp_start)
    end_timestamp = datetime_to_timestamp(timestamp_end)
    url = 'https://graphs.coinmarketcap.com/currencies/bitcoin'
    return f'{url}/{start_timestamp}/{end_timestamp}/'


def get_crypto_historical_data(string_startdate, string_enddate):
    pass
    # ts = datetime_to_timestamp(startdate)
    # return(ts)


# input start_date and end_date, automatically adds time(00:00:00)
# for loop that increases one hour (timedelta(hours=1))
# generate csv of all the urls to loop through based on start_date and end_date
# loop to get data from each hour between start_date and end_date

# r = requests.get(url)
# print(r.headers)
