from django.conf.urls import handler404
from django.urls import path

from .views import *

urlpatterns = [
    path('', name = 'home'),
]