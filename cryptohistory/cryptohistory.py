import time
from datetime import datetime

# convert datetime to unix timestamp
# 2018-01-31 01:58:11:00

# convert string date to datetime object
def convert_datetime_to_timestamp(string_datetime):
    converted_datetime = datetime.strptime(string_datetime, '%Y-%m-%d %H:%M:%S')
    dt = time.mktime(converted_datetime.timetuple())
    return int(dt) * 1000

print(convert_datetime_to_timestamp('2016-05-10 23:57:44'))
print(convert_datetime_to_timestamp('2016-6-15 23:57:44'))

# https://graphs.coinmarketcap.com/currencies/bitcoin/n1/n2/
