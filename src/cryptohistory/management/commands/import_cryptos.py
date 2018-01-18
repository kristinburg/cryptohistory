from datetime import timedelta

from django.core.management.base import BaseCommand

from cryptohistory.utils import BTC, get_crypto_historical_data


class Command(BaseCommand):
    help = 'Import cryptos'

    def handle(self, *args, **options):
        start_date = '2013-04-28'
        end_date = '2018-01-18'
        currency = BTC
        delta = timedelta(days=1)

        get_crypto_historical_data(start_date, end_date, delta, currency)
