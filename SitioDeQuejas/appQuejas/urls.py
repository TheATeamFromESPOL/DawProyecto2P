from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    path(r'', views.cargarNoticias,name='index'),
    path(r'quienesSomos/',views.quienesSomos,name='quienesSomos'),
    path(r'categorias/',views.categorias,name='categorias'),
    path(r'registro/',views.registro,name='registro'),
    path(r'iniciarSesion/',views.iniciarSesion,name='iniciarSesion'),
    path(r'salirSesion/',views.salirSesion,name='salirSesion'),
    path(r'contactenos/',views.contactenos,name='contactenos'),
    url(r'^perfil/',views.perfil,name='perfil'),
    url(r'^user/<username>/',views.pagUsuario,name='pagUsuario'),
    url(r'^noticia/(?P<pk>[0-9]+)/$', views.noticiaSeleccionada, name="noticia"),
    url(r'^ajax/enviarQuejas/$', views.ListarQuejas.as_view(), name='cargar'),
    url(r'^ajax/cargarNoticia/$', views.DetalleQuejas.as_view(), name='cargarNoticia'),
]
