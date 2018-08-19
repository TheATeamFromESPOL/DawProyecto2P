from rest_framework import serializers
from .models import *

"""
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombre')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nombreDeUsuario', 'nombrePersona', 'apellidoPersona', 'correo', 'numeroContacto','tipo')

class QuejaSerializer(serializers.ModelSerializer):
	user = serializers.ReadOnlyField(source='User.nombreDeUsuario')
	categoria = serializers.ReadOnlyField(source='categoria.nombre')
	class Meta:
		model = Queja
		fields = ('id', 'titulo', 'categoria', 'fechaCreacion', 'imagen', 'descripcion','user')

class ComentarioSerializer(serializers.ModelSerializer):
    usuario = serializers.ReadOnlyField(source='usuario.nombreDeUsuario')
    queja = serializers.ReadOnlyField(source='queja.titulo')
    class Meta:
    	model = Comentario
    	fields = ('id', 'contenido', 'user', 'fechaCreacion', 'queja')
"""