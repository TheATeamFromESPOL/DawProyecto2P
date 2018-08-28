from rest_framework import serializers
from .models import *

class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaReporte
        fields = ( 'nombreCategoria', 'usuarioId')
