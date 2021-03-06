from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    path(r'', views.cargarNoticias,name='index'),
    path(r'quienesSomos/',views.quienesSomos,name='quienesSomos'),
    path(r'categorias/',views.reportesCategorias,name='categorias'),
    #path(r'categorias/',views.categorias,name='categorias'),
    path(r'categorias/<tipo>',views.categoriaQuejas,name='categoriaQuejas'),
    path(r'registro/',views.registro,name='registro'),
    path(r'iniciarSesion/',views.iniciarSesion,name='iniciarSesion'),
    path(r'salirSesion/',views.salirSesion,name='salirSesion'),
    path(r'contactenos/',views.contactenos,name='contactenos'),
    path(r'perfil/',views.perfil,name='perfil'),
    url(r'^user/<username>/',views.pagUsuario,name='pagUsuario'),
    url(r'^noticia/(?P<pk>[0-9]+)/$', views.noticiaSeleccionada, name="noticia"),
    url(r'^ajax/administarQuejas/$', views.ListarQuejas.as_view()),
    url(r'^ajax/cargarNoticia/$', views.DetalleQuejas.as_view(), name='cargarNoticia'),
    url(r'^ajax/categorias/$', views.Listarcategorias.as_view()),
    url(r'^ajax/CategoriaDetalle/(?P<pk>[0-9]+)/$', views.DetalleCategoria.as_view()),
<<<<<<< HEAD
    url(r'^ajax/CategoriaReporte/',views.ListarReportes.as_view(),name='reporteCategorias'),

=======
    url(r'^perfil/editQueja/(?P<pk>[0-9]+)/$', views.quejaAccion,name='accionQueja'),
    url(r'^perfil/eliminarQueja/(?P<pk>[0-9]+)/$', views.eliminarQueja,name='eliminarQueja'),
>>>>>>> 6e68dd65de551a109e324f7a7cc2b5fef5db2bd3
]
