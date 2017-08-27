from django.shortcuts import render

from main.scrapper import *
from main.utils import check_domain


def index(request):
    return render(request, 'index.html', {})


def landing_view(request, slug):
    name = request.GET.get('name')
    keyword = request.GET.get('keyword')

    p = Parser()

    if not check_domain(name):
        return render(request, 'error.html')

    if not name:
        name = p.get_name()
    ctx = {
        'name': name,
        #'object': p,
        'logo': p.get_logo(name, keyword),
        'slogan': p.get_slogan(name),

    }
    return render(request, 'site2.html', ctx)
