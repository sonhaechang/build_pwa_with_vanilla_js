from pathlib import Path

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def service_worker(request):
    return HttpResponse(
        open(Path(__file__).resolve().parent / 'templates/core/service_worker.js'
    ).read(), content_type='application/javascript')

def manifest(request):
    return render(request, 'core/manifest.json', content_type='application/json')