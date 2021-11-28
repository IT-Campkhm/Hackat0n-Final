from django.shortcuts import render
from .models import *
import folium

def general(request):
    c = Category.objects.all()
    m = folium.Map()
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
    context = {
        'title': 'Список івентів',
        't': 'test'
    }
    return render(request, 'jorneyisa/table.html', context)