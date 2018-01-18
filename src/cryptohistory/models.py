from django.db import models


class Entry(models.Model):
    dt = models.DateTimeField(null=True)
    coin = models.CharField(default='UNKNOWN', max_length=12)

    market_cap = models.PositiveIntegerField(null=True)
    price_btc = models.DecimalField(
        null=True, decimal_places=11, max_digits=22)
    price_usd = models.DecimalField(
        null=True, decimal_places=11, max_digits=22)
    volume = models.PositiveIntegerField(null=True)

    class Meta:
        unique_together = ('dt', 'coin')
