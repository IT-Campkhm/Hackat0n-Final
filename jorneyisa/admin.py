from django.contrib import admin
from .models import *

class EventsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time', 'place')
    list_display_links = ('title',)
    search_fields = ('title', 'time', 'place',)
    list_filter = ('title', 'time', 'place')

admin.site.register(Events, EventsAdmin)
