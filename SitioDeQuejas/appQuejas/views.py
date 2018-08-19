from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

#from .serializers import *


def cargarNoticias(request):
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

def noticiaSeleccionada(request,pk):
    data = Queja.objects.get(pk)

    return render(request, 'appQuejas/noticia.html',{})

@permission_classes((permissions.AllowAny,))
class cargarNoti(APIView):
	def get(self, request, format=None):
		queryset=Queja.objects.all()
		queryset=queryset[:6]
		serializer = QuejaSerializer(queryset, many=True)
		return Response(serializer.data)
