from datetime import datetime

import pytest

from cryptohistory.utils import (
    BTC, ETH, generate_currency_api_urls, response_to_csv_rows,
    validate_currency
)

pytestmark = pytest.mark.django_db(transaction=True)


def test_validate_currency():
    assert validate_currency(BTC) is None
    assert validate_currency(ETH) is None

    with pytest.raises(ValueError):
        assert validate_currency('foo')

    with pytest.raises(ValueError):
        assert validate_currency(None)


def test_generate_currency_api_urls_1_day():
    start = datetime(
        year=2018, month=1, day=1, hour=0, minute=00, second=0,
        microsecond=0)
    end = datetime(
        year=2018, month=1, day=2, hour=0, minute=00, second=0,
        microsecond=0)

    expected = [
        'https://graphs2.coinmarketcap.com/currencies/bitcoin/1514761200000/1514847600000/',  # noqa
        'https://graphs2.coinmarketcap.com/currencies/bitcoin/1514847600000/1514934000000/',  # noqa
    ]
    result = generate_currency_api_urls(start, end, currency=BTC)

    assert result == expected


def test_generate_currency_api_urls_4_days():
    start = datetime(
        year=2018, month=1, day=1, hour=0, minute=00, second=0,
        microsecond=0)
    end = datetime(
        year=2018, month=1, day=4, hour=0, minute=00, second=0,
        microsecond=0)

    expected = [
        'https://graphs2.coinmarketcap.com/currencies/bitcoin/1514761200000/1514847600000/',  # noqa
        'https://graphs2.coinmarketcap.com/currencies/bitcoin/1514847600000/1514934000000/',  # noqa
        'https://graphs2.coinmarketcap.com/currencies/bitcoin/1514934000000/1515020400000/',  # noqa
        'https://graphs2.coinmarketcap.com/currencies/bitcoin/1515020400000/1515106800000/',  # noqa
    ]

    result = generate_currency_api_urls(start, end, currency=BTC)

    assert result == expected


def test_generate_currency_api_urls_365_days():
    start = datetime(
        year=2017, month=1, day=1, hour=0, minute=00, second=0,
        microsecond=0)
    end = datetime(
        year=2017, month=12, day=31, hour=0, minute=00, second=0,
        microsecond=0)

    result = generate_currency_api_urls(start, end, currency=BTC)

    assert len(result) == 365


def test_response_to_csv_rows():
    example_response = {
        "market_cap_by_available_supply":
            [
                [1512083052000, 168480198487],
                [1512083353000, 169212161618],
            ],
        "price_btc":
            [
                [1512083052000, 1.0],
                [1512083353000, 1.0],
            ],
        "price_usd":
            [
                [1512083052000, 10081.7],
                [1512083353000, 10125.5],
            ],
        "volume_usd":
            [
                [1512083052000, 8438670000],
                [1512083353000, 8478910000],
            ]
    }

    assert response_to_csv_rows(example_response) == [
        [1512083052000, 168480198487, 1.0, 10081.7, 8438670000],
        [1512083353000, 169212161618, 1.0, 10125.5, 8478910000],
    ]
