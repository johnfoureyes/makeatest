from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^Campi', views.lista_campi, name='lista_campi'),
]