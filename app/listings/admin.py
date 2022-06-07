"""Module to define models' management in admin site."""

from django.contrib import admin

from listings.models import Band, Listing

class BandAdmin(admin.ModelAdmin):
    """Model to manage band in admin site."""

    list_display = ('name', 'genre', 'year_formed')


class ListingAdmin(admin.ModelAdmin):
    """Model to manage listing in admin site."""

    list_display = ('title', 'type', 'sold', 'year', 'band')


admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)
