from django.shortcuts import render
from .models import *

def cargarNoticias(request):
	return render(request,'appQuejas/noticiasIndex.html',{})

def quienesSomos(request):
	return render(request, 'appQuejas/quienesSomos.html',{})

def categorias(request):
	return render(request, 'appQuejas/categorias.html',{})

def registro(request):
	return render(request, 'appQuejas/registro.html',{})

def iniciarSesion(request):
	return render(request, 'appQuejas/iniciarSesion.html',{})

def contactenos(request):
	return render(request, 'appQuejas/contactenos.html',{})
