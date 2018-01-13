import time


def stringdate_to_datetime(string_dt, fmt='%Y-%m-%d %H:%M:%S'):
    """
    Convert string datetime with given format to DateTime object.
    :param string_dt str: date as string
    :param fmt str: date format that string_dt is formatted in

    :return: converted DateTime object
    :rtype: DateTime
    """
    return time.strptime(string_dt, fmt)


def datetime_to_timestamp(dt):
    """
    Convert DateTime object to timestamp in milliseconds.

    :param dt DateTime

    :return: timestamp in milliseconds
    :rtype: int
    """
    return int(dt.timestamp()) * 1000


def stringdate_to_string_datetime(string_date, end=False):
    """
    Append time to string_date.

    :param string_date str
    :param end boolean: end of the day or starting of the day?

    :return: string_datetime
    :rtype: str
    :raises ValueError: if string_date is not a valid string date
    """
    validate_date_string(string_date)
    if end:
        return '{0} 23:59:59'.format(string_date)
    return '{0} 00:00:00'.format(string_date)


def validate_date_string(value):
    """
    Validate if given value is a valid formatted date.
    :param value str

    :return: None
    :raises ValueError: if value is not a valid string date
    """
    try:
        time.strptime(value, '%Y-%m-%d')
    except (ValueError, TypeError):
        raise ValueError('Incorrect data format, should be YYYY-MM-DD')
