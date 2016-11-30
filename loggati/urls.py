from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pagina_login', views.pagina_login, name='login'),
    url(r'^loggato', views.loggati, name='loggato'),
    url(r'^area_riservata', views.area_riservata, name='area_riservata'),
    url(r'^do_logout', views.do_logout, name='do_logout'),
]
