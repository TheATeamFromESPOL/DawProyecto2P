from django.shortcuts import render,redirect,render_to_response,get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.contrib.auth import authenticate,login,logout
from .serializers import *
from django.contrib.auth.models import User

def cargarNoticias(request):
	usuario = request.session.get('username',None)
	quejas=Queja.objects.all()
	queryset=quejas[:6]
	return render(request,'appQuejas/noticiasIndex.html',{"quejas":queryset})

def noticiaSeleccionada(request,pk):
	queja=Queja.objects.get(pk=pk)
	return render(request, 'appQuejas/noticia.html',{'queja':queja})
	
def quienesSomos(request):
	#Esto es lo mismo siempre
	return render(request, 'appQuejas/quienesSomos.html',{})

def categorias(request):
	return render(request, 'appQuejas/categorias.html',{})

def registro(request):
	if request.method == 'POST':
		print("scscscv")
		contraseña = request.POST.get('password')==request.POST.get('passwordRepeat');
		try:
			usuario = User.objects.get(username=request.POST.get('nombreUsuario'))
		except User.DoesNotExist:
		    usuario = None
		print(usuario,contraseña)
		if(usuario!=None):
			return render(request, 'appQuejas/registro.html',{'mensaje':'Usuario ya Registrado'})
		elif(contraseña!=True):
			return render(request, 'appQuejas/registro.html',{'mensaje':'Contraseñas no coinciden'})
		else:
			user = User.objects.create_user(request.POST.get('nombreUsuario'),request.POST.get('correoUsuario'),request.POST.get('password'))
			return redirect("/")
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
	return redirect("/")

def contactenos(request):
	#Solo es un formulario de contacto.
	#Si el usuario está loggeado, varios de los campos se deberían de sobreescribir con los datos del usuario.
	return render(request, 'appQuejas/contactenos.html',{})



@permission_classes((permissions.AllowAny,))
class ListarQuejas(APIView):
	def get(self, request, format=None):
		queryset=Queja.objects.all()
		queryset=queryset[:6]
		serializer = QuejaSerializer(queryset, many=True)
		return Response(serializer.data)

@permission_classes((permissions.AllowAny,))
class DetalleQuejas(APIView):
	def get_object(self, pk):
		try:
			return Queja.objects.get(pk=pk)
		except Queja.DoesNotExist:
			raise Http404
	def get(self, request, pk, format=None):
		queja = self.get_object(pk)
		serializer = QuejaSerializer(snippet)
		return Response(serializer.data)
	def put(self, request, pk, format=None):
		queja = self.get_object(pk)
		serializer = QuejaSerializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		queja = self.get_object(pk)
		queja.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)