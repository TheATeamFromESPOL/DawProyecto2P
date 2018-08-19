from rest_framework import serializers
from .models import *

class UsertypeSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Usertype
        fields = ('id', 'tipoUsuario')

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombre')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nombreDeUsuario', 'nombrePersona', 'apellidoPersona', 'correo', 'numeroContacto','tipo')

class QuejaSerializer(serializers.ModelSerializer):
	usuario = serializers.ReadOnlyField(source='usuario.nombreDeUsuario')
	categoria = serializers.ReadOnlyField(source='categoria.nombre')
	class Meta:
		model = Queja
		fields = ('id', 'titulo', 'categoria', 'fechaCreacion', 'imagen', 'descripcion','usuario')

class ComentarioSerializer(serializers.ModelSerializer):
    usuario = serializers.ReadOnlyField(source='usuario.nombreDeUsuario')
    queja = serializers.ReadOnlyField(source='queja.titulo')
    class Meta:
    	model = Comentario
    	fields = ('id', 'contenido', 'usuario', 'fechaCreacion', 'queja')
