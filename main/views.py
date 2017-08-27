from django.shortcuts import render

from main.scrapper import *
from main.utils import check_domain


def index(request):
    return render(request, 'index.html', {})


def landing_view(request, slug):
    if request.POST.get('name'):
        name = request.POST.get('name')
    else:
        #name = get_name()
        name = ''
    if not check_domain(name):
        return render(request, 'error.html')
    ctx = {
        'name': name,
        'logo': ''#get_logo(name),
    }
    return render(request, 'arsha.html', ctx)
