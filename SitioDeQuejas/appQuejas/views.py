from django.shortcuts import render
from .models import *

def serviciosListar(request):
	return render(request,'servicios/index.html',{'personas':personas})
