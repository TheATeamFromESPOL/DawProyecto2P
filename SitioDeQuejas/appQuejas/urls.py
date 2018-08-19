from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    path(r'', views.cargarNoticias,name='index'),
    path(r'quienesSomos/',views.quienesSomos,name='quienesSomos'),
    path(r'categorias/',views.categorias,name='categorias'),
    path(r'registro/',views.registro,name='registro'),
    path(r'iniciarSesion/',views.iniciarSesion,name='iniciarSesion'),
    path(r'contactenos/',views.contactenos,name='contactenos'),
    url(r'^noticia/(?P<pk>[0-9]+)/$', views.noticiaSeleccionada, name='queja_detalle'),
    url(r'^ajax/enviarQuejas/$', views.cargarNoti.as_view(), name='cargar'),
]
