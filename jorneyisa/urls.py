from django.conf.urls import handler404
from django.urls import path

from .views import *

urlpatterns = [
    path('map/', general, name = 'home'),
    path('tabel/', showtable, name = 'tabel'),
]
