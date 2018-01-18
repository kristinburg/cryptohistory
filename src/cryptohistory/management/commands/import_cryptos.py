from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Import cryptos'

    def handle(self, *args, **options):
        print('hi')
