from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login as lg, authenticate
from django.contrib import messages


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