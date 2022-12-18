from django.urls import path, re_path
from core import views

app_name = 'core'
urlpatterns = [
	path('', views.index, name='index'),
    re_path(r'^service_worker\.js$', views.service_worker, name='serviceworker'),
    re_path(r'^manifest\.json$', views.manifest, name='manifest'),
]