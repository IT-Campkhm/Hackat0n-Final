from django.shortcuts import render

def general(request):
    return render(
        request,
        'jorneyisa/index.html',
        {
            'title': 'Головна сторінка',
        }
    )