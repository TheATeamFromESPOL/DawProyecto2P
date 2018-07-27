from django.db import models

# Create your models here.
class Usuario(models.Model):

class Categoria(models.Model):

class Queja(models.Model):
		titulo = models.charField(max_length=100)

class Comentario(models.Model):