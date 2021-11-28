from django.shortcuts import render
from .models import *
import folium
import folium.features
import geocoder


def general(request):

    ukrain = geocoder.osm('UA')

    m = folium.Map(location=[ukrain.latlng[0], ukrain.latlng[1]], zoom_start=7)

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

    citys = [kiev, kharkiv, odessa, lviv, zhytomyr, khmelnytskyi,
             ivano_frankivsk, vinnitsa, zaporizhzhia, сhernihiv]
    events = Events.objects.all()

    for city, event in citys, events:
        folium.Marker(
            [citys[city].latlng[0], citys[city].latlng[1]],
            popup=f'{event.title}',
            tooltip='Дізнатися більше про івент.'
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
