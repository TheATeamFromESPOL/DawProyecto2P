from djongo import models
from django import forms

class CategoriaReporte(models.Model):
	nombreCategoria = models.IntegerField()
	usuarioId = models.IntegerField()
	