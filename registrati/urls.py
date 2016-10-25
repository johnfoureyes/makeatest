from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^registrazione', views.registrazione, name='registrazione'),
    url(r'^registrati', views.registrati, name='registrati'),
]
