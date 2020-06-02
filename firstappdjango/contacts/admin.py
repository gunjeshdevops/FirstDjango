from django.contrib import admin
from .models import Contacts


# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contacts_date')
    list_diaplay_links = ('id', 'name')
    search_fileds = ('name', 'email', 'listing')
    list_per_page = 25


admin.site.register(Contacts, ContactAdmin)
