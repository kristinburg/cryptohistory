import time
from datetime import datetime
import requests


# convert string_date to datetime object
def convert_stringdate_to_datetime(string_datetime):
    converted_datetime = datetime.strptime(string_datetime, '%Y-%m-%d %H:%M:%S')
    return converted_datetime

# convert string date to integer in milliseconds (for url)
def convert_datetime_to_ms_integer(string_datetime):
    dt = convert_stringdate_to_datetime(string_datetime)
    return int(dt) * 1000


def generate_bitcoin_url_by_dates(timestamp_start, timestamp_end):
    starttime = convert_datetime_to_ms_integer(timestamp_start)
    endtime = convert_datetime_to_ms_integer(timestamp_end)
    url = 'https://graphs.coinmarketcap.com/currencies/bitcoin/'
    return (f'{url}{str(starttime)}/{str(endtime)}')


def get_crypto_historical_data(string_startdate, string_enddate):
    pass
    # ts = convert_datetime_to_timestamp(startdate)
    # return(ts)

# get_crypto_historical_data('2017-05-10', '2017-05-11')

# input starttime and endtime (date to date), automatically adds time
# for loop that increases one hour (timedelta(hours=1))
# generate csv of all the urls to loop through based on starttime and endtime
# loop to get data from each hour between starttime and endtime

# r = requests.get(url)
# print(r.headers)
