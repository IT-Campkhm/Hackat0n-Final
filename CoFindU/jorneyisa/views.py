from django.shortcuts import render
import folium

def general(request):
    m = folium.Map()
    m = m._repr_html_()
    context = {
        'title': 'Головна сторінка',
        'map': m
    }
    return render(
        request,
        'jorneyisa/map.html',
        context
    )