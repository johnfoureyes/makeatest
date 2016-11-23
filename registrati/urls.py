from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^registrazione', views.registrazione, name='registrazione'),
    url(r'^registrati', views.registrati, name='registrati'),
]
