from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import *
#from .serializers import *

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def cargarNoticias(request):
	if request.method == 'GET':
		#Debe cargar las quejas. Las más recientes deben colocarse en la primera página, y las últimas en la última página.
		#O podemos seguir el ejemplo de 9gag.com. Añade más "items" mientras bajamos por la página.
	return render(request,'appQuejas/noticiasIndex.html',{})

def quienesSomos(request):
	#Esto es lo mismo siempre
	return render(request, 'appQuejas/quienesSomos.html',{})

def categorias(request):
	return render(request, 'appQuejas/categorias.html',{})

def registro(request):
	return render(request, 'appQuejas/registro.html',{})

def iniciarSesion(request):
	return render(request, 'appQuejas/iniciarSesion.html',{})

def contactenos(request):
	#Solo es un formulario de contacto.
	#Si el usuario está loggeado, varios de los campos se deberían de sobreescribir con los datos del usuario.
	return render(request, 'appQuejas/contactenos.html',{})
