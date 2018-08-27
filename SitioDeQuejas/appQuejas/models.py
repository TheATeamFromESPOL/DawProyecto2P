from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Persona(models.Model):
	user = models.OneToOneField(User,related_name='persona', on_delete=models.CASCADE)
	nombrePersona = models.CharField(max_length=255)
	apellidoPersona = models.CharField(max_length=255)
	profesion = models.CharField(max_length=100)
	numeroContacto = models.CharField(max_length=50)

class Queja(models.Model):
	titulo = models.CharField(max_length=300)
	categoria = models.ForeignKey('Categoria',related_name='quejas',on_delete=models.CASCADE)
	fechaCreacion = models.DateField(auto_now_add=True,editable=False)
	imagen = models.CharField(max_length=500,default="imagencita")
	descripcion = models.CharField(max_length=1000)
	usuario = models.ForeignKey(User,related_name='queja',on_delete=models.CASCADE,editable=False)

	class Meta:
		ordering = ['-fechaCreacion']

	def __unicode__(self):
		return '%d: %s' % (self.pk, self.titulo)

class Categoria(models.Model):
	nombre = models.CharField(max_length=100)
	def __str__(self):
		return '%s' % (self.nombre)

class Comentario(models.Model):
	contenido = models.CharField(max_length=500)
	usuario = models.ForeignKey(User,on_delete=models.CASCADE)
	fechaCreacion = models.DateField(auto_now=True)
	queja = models.ForeignKey('Queja',on_delete=models.CASCADE)
