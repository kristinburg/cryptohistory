from django.contrib import admin

from crypto.models import Entry


class EntryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Entry, EntryAdmin)
