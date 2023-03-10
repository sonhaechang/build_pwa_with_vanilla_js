from django.conf import settings
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def service_worker(request):
    return render(request, 'core/service_worker.js', {
        'static': settings.STATIC_URL}, content_type='application/javascript')

def manifest(request):
    return render(request, 'core/manifest.json', {
        'static': settings.STATIC_URL}, content_type='application/json')