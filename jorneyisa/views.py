from django.shortcuts import render
from .models import *
import folium
import geocoder


def general(request):
    
    ukrain = geocoder.osm('UA')
    
    m = folium.Map(location = [ukrain.latlng[0], ukrain.latlng[1]], zoom_start = 7)
    
    kiev = geocoder.osm('Kiev')
    kharkiv = geocoder.osm('Kharkiv')
    odessa = geocoder.osm('Odessa')
    lviv = geocoder.osm('Lviv')
    zhytomyr = geocoder.osm('Zhytomyr')
    khmelnytskyi = geocoder.osm('Khmelnytskyi')
    ivano_frankivsk = geocoder.osm('Ivano-Frankivsk')
    vinnitsa = geocoder.osm('Vinnitsa')
    zaporizhzhia = geocoder.osm('Zaporizhzhia')
    сhernihiv = geocoder.osm('Chernihiv')
    
    
    folium.Marker(
        [kiev.latlng[0], kiev.latlng[1]],
        popup = 'Дізнатися більше.',
        tooltip = ''
    ).add_to(m)
    
    folium.Marker(
        [kharkiv.latlng[0], kharkiv.latlng[1]],
        popup = 'Дізнатися більше.',
        tooltip = ''
    ).add_to(m)
    
    folium.Marker(
        [odessa.latlng[0], odessa.latlng[1]],
        popup = 'Дізнатися більше.',
        tooltip = ''
    ).add_to(m)
    
    folium.Marker(
        [lviv.latlng[0], lviv.latlng[1]],
        popup = 'Дізнатися більше.',
        tooltip = ''
    ).add_to(m)
    
    folium.Marker(
        [zhytomyr.latlng[0], zhytomyr.latlng[1]],
        popup = 'Дізнатися більше.',
        tooltip = ''
    ).add_to(m)
    
    folium.Marker(
        [khmelnytskyi.latlng[0], khmelnytskyi.latlng[1]],
        popup = 'Дізнатися більше.',
        tooltip = ''
    ).add_to(m)
    
    folium.Marker(
        [ivano_frankivsk.latlng[0], ivano_frankivsk.latlng[1]],
        popup = 'Дізнатися більше.',
        tooltip = ''
    ).add_to(m)
    
    folium.Marker(
        [vinnitsa.latlng[0], vinnitsa.latlng[1]],
        popup = 'Дізнатися більше.',
        tooltip = ''
    ).add_to(m)
    
    folium.Marker(
        [zaporizhzhia.latlng[0], zaporizhzhia.latlng[1]],
        popup = 'Дізнатися більше.',
        tooltip = ''
    ).add_to(m)
    
    
    folium.Marker(
        [сhernihiv.latlng[0], сhernihiv.latlng[1]],
        popup = 'Дізнатися більше.',
        tooltip = ''
    ).add_to(m)
    
    
    m = m._repr_html_()

    context = {
        'title': 'Знайди івент',
        'map': m,
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
