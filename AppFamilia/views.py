from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar
from .models import Familiar1
from .models import Familiar2

# Create your views here.

def familiar(request):
    familiar=Familiar(nombre= "Rolando", apellido= "Rodriguez", edad= 46, profesion= "comerciante",)
    familiar.save()
    texto=f"Familiar Creado: nombre {familiar.nombre} apellido {familiar.apellido} edad {familiar.edad}"
    return HttpResponse(texto)
    

def familiar1(request):
    familiar1=Familiar1(nombre= "Paulina", apellido= "Rodriguez", edad= 45, profesion= "comerciante",)
    familiar1.save()
    texto=f"Familiar Creado: nombre {familiar1.nombre} apellido {familiar1.apellido} edad {familiar1.edad}" 
    return HttpResponse(texto)
    

def familiar2(request):
    familiar2=Familiar2(nombre= "Mariano", apellido= "Rodriguez", edad= 17, profesion= "estudiante",)
    familiar2.save()
    texto=f"Familiar Creado: nombre {familiar2.nombre} apellido {familiar2.apellido} edad {familiar2.edad}"
    return HttpResponse(texto)


def Inicio(request):
    return render (request, "AppFamilia/Inicio.html")

def familiares(request):
    return render (request, "AppFamilia/familiares.html")

def familiares1(request):
    return render (request, "AppFamilia/familiares1.html")

def familiares2 (request):
    return render (request, "AppFamilia/familiares2.html")

