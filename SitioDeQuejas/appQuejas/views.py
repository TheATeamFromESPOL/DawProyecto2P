from django.shortcuts import render,redirect,render_to_response,get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect 
from .forms import *
from .serializers import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from rest_framework.renderers import TemplateHTMLRenderer

from reportes.models import *
from reportes.serializers import *

def reportesCategorias(request):
	listaCategorias = CategoriaReporte.objects.all()
	categoria = Categoria.objects.all()
	persona = Persona.objects.all()
	print("aquiíiiiiii")
	print(listaCategorias)
	print(categoria)
	print(persona)
	return render(request,'appQuejas/categorias.html',{"listaCategorias":listaCategorias,"categoria":categoria,"persona":persona})

def cargarNoticias(request):
	listaQuejas=Queja.objects.all()
	paginator = Paginator(listaQuejas,12) #Mostrar 12 quejas por pagina
	page = request.GET.get('page')
	quejas = paginator.get_page(page)
	return render(request,'appQuejas/noticiasIndex.html',{"quejas":quejas})

def noticiaSeleccionada(request,pk):
	queja=Queja.objects.get(pk=pk)
	return render(request, 'appQuejas/noticia.html',{'queja':queja})
	
def quienesSomos(request):
	#Esto es lo mismo siempre
	return render(request, 'appQuejas/quienesSomos.html',{})

def categoriaQuejas(request,tipo):
	listaCategorias = Categoria.objects.all()
	categoria = Categoria.objects.get(nombre=tipo)
	listaQuejas = Queja.objects.filter(categoria_id=categoria.id).order_by('-fechaCreacion')
	paginator = Paginator(listaQuejas,6) #Mostrar 12 quejas por pagina
	page = request.GET.get('page')
	quejas = paginator.get_page(page)
	return render(request, 'appQuejas/categorias.html',{"listaCategorias":listaCategorias,"quejas": quejas,"mensaje":""})

def registro(request):
	if request.method == 'POST':
		contraseña = request.POST.get('password')==request.POST.get('passwordRepeat');
		try:
			usuario = User.objects.get(username=request.POST.get('nombreUsuario'))
		except User.DoesNotExist:
		    usuario = None
		print(usuario,contraseña)
		if(usuario!=None):
			return render(request, 'appQuejas/registrso.html',{'mensaje':'Usuario ya Registrado'})
		elif(contraseña!=True):
			return render(request, 'appQuejas/registro.html',{'mensaje':'Contraseñas no coinciden'})
		elif(len(request.POST.get('password'))==0):
			return render(request, 'appQuejas/registro.html',{'mensaje':'Campo contraseña vacio'})
		else:
			user = User.objects.create_user(request.POST.get('nombreUsuario'),request.POST.get('correoUsuario'),request.POST.get('password'))
			render(request, 'appQuejas/iniciarSesion.html',{"mensaje":"Usuario exitosamente creado, ahora puede iniciar sesion xD"})

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
	return redirect("index")

def contactenos(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			send_mail(
				data['subject'],
				data['content'],
				'theateam.daw@gmail.com', #FROM
				[data['email']],
				fail_silently=False,
			)
			return HttpResponseRedirect('/contactenos/')
	else:
        	form = ContactForm()
 
	return render(request, 'appQuejas/contactenos.html', {'form': form})

@permission_classes((permissions.AllowAny,))
class ListarReportes(APIView):
	def get(self, request, format=None):
		queryset=CategoriaReporte.objects.all()
		
		serializer = ReporteSerializer(queryset, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		print("entra ListarReporte Post")
		print(request.data)
		
		print(ReporteSerializer(data=request.data))
		serializer = ReporteSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes((permissions.AllowAny,))
class ListarQuejas(APIView):
	def get(self, request, format=None):
		queryset=Queja.objects.all()
		serializer = QuejaSerializer(queryset, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		print(request.data)		
		serializer = QuejaSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	

@permission_classes((permissions.AllowAny,))
class DetalleQuejas(APIView):
	def get_object(self, pk):
		try:
			return Queja.objects.get(pk=pk)
		except Queja.DoesNotExist:
			raise Http404
	def get(self, request, pk, format=None):
		snippet = self.get_object(pk)
		serializer = QuejaSerializer(snippet)
		return Response(serializer.data)

@permission_classes((permissions.AllowAny,))
class DetalleCategoria(APIView):
	def get_object(self, pk):
		try:
			return Categoria.objects.get(pk=pk)
		except Categoria.DoesNotExist:
			raise Http404
	
	def get(self, request, pk, format=None):
		categoria = self.get_object(pk)
		serializer = CategoriaSerializer(categoria)
		return Response(serializer.data)

def perfil(request):
	if not request.user.is_authenticated:
		return render(request, 'appQuejas/perfil.html')
	usuario = request.user.id
	persona = Persona.objects.get(user=usuario)
	listaQuejas = Queja.objects.filter(usuario_id=usuario).order_by('-fechaCreacion')
	return render(request, 'appQuejas/perfil.html',{"persona":persona,"listaQuejas":listaQuejas})

def pagUsuario(request):
	return

@permission_classes((permissions.AllowAny,))
class Listarcategorias(APIView):
	def get(self, request, format=None):
		queryset=Categoria.objects.all()
		serializer = CategoriaSerializer(queryset, many=True)
		return Response(serializer.data)


def quejaAccion(request,pk):
	if request.method == "GET":
		queja = get_object_or_404(Queja,pk=pk)
		form = QuejaForm(instance = queja)
		return render(request, 'appQuejas/editQueja.html',{"queja":queja,"form":form})
	elif request.method == "POST":
		queja = get_object_or_404(Queja,pk=pk)
		form = QuejaForm(request.POST,instance=queja)
		if form.has_changed():
			print("cambio")
			if form.is_valid():
				print("es valido")
				form.save()
				usuario = request.user.id
				persona = Persona.objects.get(user=usuario)
				listaQuejas = Queja.objects.filter(usuario_id=usuario).order_by('-fechaCreacion')
				return render(request, 'appQuejas/perfil.html',{"persona":persona,"listaQuejas":listaQuejas})
	return redirect('perfil')

def eliminarQueja(request,pk):
	if request.method == "POST":
		queja = get_object_or_404(Queja,pk=pk)
		queja.delete()
	usuario = request.user.id
	persona = Persona.objects.get(user=usuario)
	listaQuejas = Queja.objects.filter(usuario_id=usuario).order_by('-fechaCreacion')
	return render(request, 'appQuejas/perfil.html',{"persona":persona,"listaQuejas":listaQuejas,"eliminacion":True})


