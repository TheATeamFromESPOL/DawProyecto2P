from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Persona)
admin.site.register(Categoria)
admin.site.register(Queja)
admin.site.register(Comentario)