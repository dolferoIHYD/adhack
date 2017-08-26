from django.shortcuts import render

from scrapper import *

def index(request):
    return render(request, 'index.html', {})


def landing_view(request):
    if request.POST.get('name'):
        name = request.POST.get('name'):
    else:
        name = get_name()
    ctx = {
        'name': name,
        'logo': get_logo(name),
        ''
    }
    return render(request, 'landing.html', ctx)
