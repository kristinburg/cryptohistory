from datetime import datetime

import pytest
from date_utils import (
    datetime_to_timestamp, stringdate_to_datetime,
    stringdate_to_string_datetime, validate_date_string
)


def test_stringdate_to_datetime():
    string_dt = '2018-01-31 12:12:00'
    expected = datetime.strptime(string_dt, '%Y-%m-%d %H:%M:%S')
    assert stringdate_to_datetime(string_dt) == expected


def test_datetime_to_timestamp():
    dt = datetime(
        year=2018, month=1, day=31, hour=13, minute=00, second=5,
        microsecond=0)
    expected = 1517400005000

    assert datetime_to_timestamp(dt) == expected


def test_stringdate_to_string_datetime():
    string_date = '2018-01-31'
    expected_start = '2018-01-31 00:00:00'
    expected_end = '2018-01-31 23:59:59'

    assert stringdate_to_string_datetime(string_date) == expected_start
    assert stringdate_to_string_datetime(
        string_date, end=False) == expected_start
    assert stringdate_to_string_datetime(string_date, end=True) == expected_end

    with pytest.raises(ValueError):
        stringdate_to_string_datetime('foo')

    with pytest.raises(ValueError):
        stringdate_to_string_datetime('2018-01-31 00:00:00')


@pytest.mark.parametrize('test_input,valid', [
    ('', False),
    (None, False),
    ('2018-01-32', False),
    ('2018-01-31 00:00:00', False),
    ('2018-01-31', True),
])
def test_validate_date_string(test_input, valid):
    if valid:
        validate_date_string(test_input)
    else:
        with pytest.raises(ValueError):
            validate_date_string(test_input)
