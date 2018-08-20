from rest_framework import serializers
from .models import *



class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombre')

	
class PersonaSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Persona
        fields = ('id', 'user', 'nombrePersona', 'apellidoPersona','profesion', 'numeroContacto')

	
class QuejaSerializer(serializers.ModelSerializer):
	user = serializers.ReadOnlyField(source='user.username')
	categoria = serializers.ReadOnlyField(source='categoria.nombre')
	class Meta:
		model = Queja
		fields = ('id', 'titulo', 'categoria', 'fechaCreacion', 'imagen', 'descripcion','user')

		
class ComentarioSerializer(serializers.ModelSerializer):
    usuario = serializers.ReadOnlyField(source='user.username')
    queja = serializers.ReadOnlyField(source='queja.titulo')
    class Meta:
    	model = Comentario
    	fields = ('id', 'contenido', 'user', 'fechaCreacion', 'queja')
