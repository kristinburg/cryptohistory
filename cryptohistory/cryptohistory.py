import time
from datetime import datetime


# convert string date to datetime object
def convert_datetime_to_timestamp(string_datetime):
    converted_datetime = datetime.strptime(string_datetime, '%Y-%m-%d %H:%M:%S')
    dt = time.mktime(converted_datetime.timetuple())
    return int(dt) * 1000


def generate_url_by_dates(timestamp_start, timestamp_end):
    starttime = convert_datetime_to_timestamp(timestamp_start)
    endtime = convert_datetime_to_timestamp(timestamp_end)
    url = 'https://graphs.coinmarketcap.com/currencies/bitcoin/'
    return url + str(starttime) + '/' + str(endtime)


print(convert_datetime_to_timestamp('2017-05-10 23:57:44'))
print(convert_datetime_to_timestamp('2017-6-15 23:57:44'))
print(generate_url_by_dates('2017-05-10 23:57:44', '2017-6-15 23:57:44'))
