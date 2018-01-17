from django.db import models


class Entry(models.Model):
    timestamp = models.DateTimeField()

    coin = models.CharField(default='UNKNOWN', max_length=12)

    market_cap = models.PositiveIntegerField(null=True)
    price_btc = models.DecimalField(null=True, decimal_places=11, max_digits=11)
    price_usd = models.DecimalField(null=True, decimal_places=11, max_digits=11)
    volume = models.PositiveIntegerField(null=True)
