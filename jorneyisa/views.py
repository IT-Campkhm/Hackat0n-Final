from django.shortcuts import render
from .models import *
import folium
import geocoder


def general(request):
    g = geocoder.osm('UA')
    c = Category.objects.all()
    m = folium.Map(location = [g.latlng[0], g.latlng[1]], zoom_start = 7)
    m = m._repr_html_()

    context = {
        'title': 'Знайди івент',
        'map': m,
        'category': c
    }
    return render(
        request,
        'jorneyisa/map.html',
        context
    )


def showtable(request):
    event = Events.objects.all()
    context = {
        'title': 'Список івентів',
        'events': event
    }
    return render(
        request,
        'jorneyisa/table.html',
        context
    )
