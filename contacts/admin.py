from django.contrib import admin
from .models import Contact
# this allows us to change all the fields displayed for each 
# contact in the contact  section of the admin app (our admin area we actually sign into through the browser)
class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'listing', 'email', 'contact_date')
  list_display_links = ('id', 'name')
  search_fields = ('name', 'email', 'listing')
  list_per_page = 25
admin.site.register(Contact, ContactAdmin)

