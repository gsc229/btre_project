from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin): # this allows us to change all the fields displayed for each 
                                      # listing in the listings section of the admin app
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)