from djongo import models
from django import forms

class Categoria(models.Model):
	nombre = models.CharField(max_length=90)
