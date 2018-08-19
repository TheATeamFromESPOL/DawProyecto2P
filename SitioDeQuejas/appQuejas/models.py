from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Persona(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	nombrePersona = models.CharField(max_length=255)
	apellidoPersona = models.CharField(max_length=255)
	profesion = models.CharField(max_length=100)
	numeroContacto = models.CharField(max_length=50)

class Queja(models.Model):
	titulo = models.CharField(max_length=300)
	categoria = models.ForeignKey('Categoria',on_delete=models.CASCADE)
	fechaCreacion = models.DateField(auto_now=True)
	imagen = models.ImageField(upload_to='imgs/')
	descripcion = models.CharField(max_length=1000)
	usuario = models.ForeignKey(User,related_name='usuario',on_delete=models.CASCADE)

class Categoria(models.Model):
	nombre = models.CharField(max_length=100)

class Comentario(models.Model):
	contenido = models.CharField(max_length=500)
	usuario = models.ForeignKey(User,on_delete=models.CASCADE)
	fechaCreacion = models.DateField(auto_now=True)
	queja = models.ForeignKey('Queja',on_delete=models.CASCADE)