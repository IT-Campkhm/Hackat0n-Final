from django.conf.urls import handler404
from django.urls import path

from .views import *

urlpatterns = [
    path('', general, name = 'home'),
    path('table/', showtable, name = 'tabel_event'),
]
