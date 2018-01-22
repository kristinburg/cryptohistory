from django.contrib import admin

from cryptohistory.models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = [
        'dt', 'coin', 'market_cap', 'price_btc', 'price_usd', 'volume']
    list_filter = ['coin', ]
    date_hierarchy = 'dt'
    search_fields = ['price_usd', ]


admin.site.register(Entry, EntryAdmin)
