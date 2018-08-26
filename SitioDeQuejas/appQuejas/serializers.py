from rest_framework import serializers
from .models import *



class CategoriaSerializer(serializers.ModelSerializer):
    quejas = serializers.StringRelatedField(many=True)
    class Meta:
        model = Categoria
        fields = ('id', 'nombre','quejas')

	
class PersonaSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Persona
        fields = ('id', 'user', 'nombrePersona', 'apellidoPersona','profesion', 'numeroContacto')

	
class QuejaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queja
        fields = ( 'titulo', 'categoria', 'fechaCreacion', 'imagen', 'descripcion','usuario')

		
class ComentarioSerializer(serializers.ModelSerializer):
    usuario = serializers.ReadOnlyField(source='user.username')
    queja = serializers.ReadOnlyField(source='queja.titulo')
    class Meta:
    	model = Comentario
    	fields = ( 'contenido', 'usuario', 'fechaCreacion', 'queja')
