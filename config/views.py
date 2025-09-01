from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login as lg, authenticate, logout
from django.contrib import messages
from .forms import Regristo


#El dicionario(CONTEXT)son las variables a utlizar en el html
def index(request):
    return render(request, 'index.html', {
        "titulo": "Inicio",
        "mensaje": "Tienda",
        "personas": [
            {'titulo':'Campera', 'precio':15, 'adulto':False},
            {'titulo':'Pantalon', 'precio':11, 'adulto':True},
            {'titulo':'Remera', 'precio':18, 'adulto':False},
            {'titulo':'Gorra', 'precio':10, 'adulto':True},
        ]
    })

def login(request):

    if request.method == "POST": #Si es post, es que enviaron el formulario
        username = request.POST.get("username") #El post es un diccionario, recibimos la clave
        password = request.POST.get("password") 
        #print(f"Username: {username}, Password: {password}")
        users = authenticate(request, username=username, password=password)
        if users:
            lg(request, users) #Login
            messages.success(request, f"Login exitoso. Bienvendio {users.username}")
            return redirect(index)
        else:
            messages.error(request, "Usuario o contrasena incorrecta")

    return render(request, 'users/login.html', {})

def salir(request):
    logout(request)
    messages.success(request, "Has cerrado sesión.")
    return redirect(login)

def registro(request):
    form = Regristo() #aqui se almacenara el formulario
    return render(request, 'users/registro.html', {
        'form': form #es lo que se está mostrando en el HTML
    })