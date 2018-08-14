from django.db import models

# Create your models here.
class Usertype(models.Model):
	tipoUsuario = models.CharField(max_length=20)

class Usuario(models.Model):
	nombreDeUsuario = models.CharField(max_length=80,unique=True)
	contrasena = models.CharField(max_length=50)
	nombrePersona = models.CharField(max_length=255)
	apellidoPersona = models.CharField(max_length=255)
	correo = models.CharField(max_length=255,unique=True)
	numeroContacto = models.CharField(max_length=50)
	tipo = models.ForeignKey('Usertype',on_delete=models.CASCADE)

class Queja(models.Model):
	titulo = models.CharField(max_length=300)
	categoria = models.ForeignKey('Categoria',on_delete=models.CASCADE)
	fechaCreacion = models.DateField(auto_now=True)
	imagen = models.ImageField(upload_to='imgs/')
	descripcion = models.CharField(max_length=1000)
	usuario = models.ForeignKey('Usuario',on_delete=models.CASCADE)

class Categoria(models.Model):
	nombre = models.CharField(max_length=100)

class Comentario(models.Model):
	contenido = models.CharField(max_length=500)
	usuario = models.ForeignKey('Usuario',on_delete=models.CASCADE)
	fechaCreacion = models.DateField(auto_now=True)
	queja = models.ForeignKey('Queja',on_delete=models.CASCADE)