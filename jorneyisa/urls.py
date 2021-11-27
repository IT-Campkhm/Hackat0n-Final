from django.conf.urls import handler404
from django.urls import path

from .views import *

urlpatterns = [
    path('', general, name = 'home'),
    path('map/', showmap, name = 'map'),
    path('tabel/', showtable, name = 'tabel'),
]
