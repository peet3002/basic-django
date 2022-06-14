from django.http import HttpResponse
from django.shortcuts import render

from datetime import date

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def products(request):
    return render(request, 'products.html')

def contact(request):
    return render(request, 'contact.html')


def about(request):
    return HttpResponse('This is about page')


def search(request, keyword, page):
    return HttpResponse(f'Search for {keyword} page : {page}')

def maps(requset):
    type = requset.GET.get('type', 'hybrid')
    lat = requset.GET.get('lat', '13.039303')
    lon = requset.GET.get('lon', '100.089488')
    zoom = requset.GET.get('z', 10)
    
    return HttpResponse(f'Map type: {type}<br>Location: {lat}, {lon}<br>Zoom: {zoom}')

def test(request):
    dt = date.today()
    data = {
        'site': {'title': 'Django Framework', 'message': 'Hello Python Django'},
        'colors': ['red', 'greed', 'blue'],
        'date': dt 
    }
    return render(request, 'test.html', data)