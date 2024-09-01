from django.shortcuts import render, HttpResponse
from .models import Product

# Create your views here.
#request -> response

def home(request):
    return render(request, "home.html")

def carta(request):
    #hacer llamadas a una base de datos
    
    productos= Product.objects.all()

    return render(request, "carta.html", {"productos": productos})

def ubicaciones(request):
    return render(request, "ubicaciones.html")