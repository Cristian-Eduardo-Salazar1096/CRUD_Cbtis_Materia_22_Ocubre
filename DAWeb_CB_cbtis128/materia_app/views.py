from django.shortcuts import render

# Create your views here.
def inicio_vistia(request):
    return render(request,"gestionarMateria.html")