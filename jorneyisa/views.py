from django.shortcuts import render
from .models import *
import folium

def general(request):
    c = Category.objects.all()
    m = folium.Map()
    m = m._repr_html_()

    context = {
        'title': 'Головна сторінка',
        'map': m,
        'category': c
    }
    return render(
        request,
        'jorneyisa/index.html',
        context
    )

def showmap(request):
    return render(request, 'jorneyisa/map.html')

def showtable(request):
    return render(request, 'jorneyisa/table.html')