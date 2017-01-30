from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^Tornei', views.lista_tornei, name='lista_tornei'),
    url(r'^iscrivi_tornei', views.iscrivi_tornei, name='iscrivi_tornei'),
    url(r'^agenda', views.lista_tornei_iscritti, name='lista_tornei_iscritti'),

]
