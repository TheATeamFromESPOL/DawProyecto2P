from django.db import models

# Create your models here.
class Usuario(models.Model):
	user = models.CharField(max_length=80,unique=True)
	contrasena = models.CharField(max_length=50)
	nombrePersona = models.CharField(max_length=255)
	apellidoPersona = models.CharField(max_length=255)
	correo = models.CharField(max_length=255,unique=True)
	numeroContacto = models.CharField(max_length=50)

class Queja(models.Model):
	titulo = models.CharField(max_length=150)
	categoria = models.ForeignKey('Categoria',on_delete=models.CASCADE)
	fechaCreacion = models.DateField(auto_now=True)
	imagen = models.ImageField(upload_to='imgs/')
	usuario = models.ForeignKey('Usuario',on_delete=models.CASCADE)
	comentarios = models.ManyToManyField('Comentario')

class Categoria(models.Model):
	nombre = models.CharField(max_length=100)

class Comentario(models.Model):
	contenido = models.CharField(max_length=500)
	usuario = models.ForeignKey('Usuario',on_delete=models.CASCADE)
	fechaCreacion = models.DateField(auto_now=True)