from django.contrib import admin

from cryptohistory.models import Entry


class EntryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Entry, EntryAdmin)
