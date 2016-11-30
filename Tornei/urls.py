from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^Tornei', views.lista_tornei, name='lista_tornei'),
]
