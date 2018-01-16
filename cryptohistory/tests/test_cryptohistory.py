from cryptohistory import response_to_csv_rows


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
