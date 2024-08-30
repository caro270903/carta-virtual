from django.shortcuts import render, HttpResponse

# Create your views here.
#request -> response

def home(request):
    return render(request, "home.html")

def carta(request):
    #hacer llamadas a una base de datos

    return render(request, "carta.html", {"name": "Juan Pablo"})

def ubicaciones(request):
    return render(request, "ubicaciones.html")