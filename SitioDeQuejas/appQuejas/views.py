from django.shortcuts import render,redirect,render_to_response,get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
#from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.contrib.auth import authenticate,login

#from .serializers import *


def cargarNoticias(request):
	usuario = request.session.get('username',None)
	quejas=Queja.objects.all()
	queryset=quejas[:6]
	return render(request,'appQuejas/noticiasIndex.html',{"quejas":queryset})


def quienesSomos(request):
	#Esto es lo mismo siempre
	return render(request, 'appQuejas/quienesSomos.html',{})

def categorias(request):
	return render(request, 'appQuejas/categorias.html',{})

def registro(request):
	return render(request, 'appQuejas/registro.html',{})

def iniciarSesion(request):
	if request.method == 'POST':
		usuario = authenticate(request,username=request.POST.get('nombreUsuario'),password=request.POST.get('password'))
		if usuario is not None:
			login(request,usuario)
			return redirect("/")
		else:
			return render(request, 'appQuejas/iniciarSesion.html', {"mensaje":"Tu usuario y contraseña no coinciden. Intenta de nuevo."})
	return render(request, 'appQuejas/iniciarSesion.html',{"mensaje":""})

def salirSesion(request):
	logout(request)
	return redirect("appQuejas:cargarNoticias")

def contactenos(request):
	#Solo es un formulario de contacto.
	#Si el usuario está loggeado, varios de los campos se deberían de sobreescribir con los datos del usuario.
	return render(request, 'appQuejas/contactenos.html',{})

def noticiaSeleccionada(request,pk):
	noticia = Queja.objects.get(pk=pk)
	serializer = QuejaSerializer(noticia, many=False)
	return render(request, 'appQuejas/noticia.html',{})


@permission_classes((permissions.AllowAny,))
class cargarNoti(APIView):
	def get(self, request, format=None):
		queryset=Queja.objects.all()
		queryset=queryset[:6]
		serializer = QuejaSerializer(queryset, many=True)
		return Response(serializer.data)

@api_view(['GET'])
def cargarNoticia(request, format=None):
	noticia = Queja.objects.get(pk=pk)
	serializer = QuejaSerializer(queryset, many=True)
	return Response(serializer.data)