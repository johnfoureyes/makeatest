from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^login', views.login, name='login'),
    url(r'^loggati', views.loggati, name='loggato'),
]
