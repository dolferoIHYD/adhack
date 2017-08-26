from django.shortcuts import render

from scrapper import *

def index(request):
    return render(request, 'index.html', {})


def landing_view(request):
    name = get_name(request.POST.get('name'))
    ctx = {
        'name': name,
        'logo': get_logo(name),
        ''
    }
    return render(request, 'landing.html', ctx)
