from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login as lg, authenticate, logout
from django.contrib import messages
from .forms import Regristo
from django.contrib.auth.models import User
from products.models import Product


#El dicionario(CONTEXT)son las variables a utlizar en el html
def index(request):
    productos = Product.objects.all()  # Query para obtener todos los productos
    return render(request, 'index.html', {
        "titulo": "Inicio",
        "mensaje": "Tienda",
        "productos": productos
    })

def login(request):
    if request.user.is_authenticated:
        return redirect(index)

    if request.method == "POST": #Si es post, es que enviaron el formulario
        username = request.POST.get("username") #El post es un diccionario, recibimos la clave
        password = request.POST.get("password") 
        #print(f"Username: {username}, Password: {password}")
        users = authenticate(request, username=username, password=password)
        if users:
            lg(request, users) #Login
            messages.success(request, f"Login exitoso. Bienvenido {users.username}")
            return redirect(index)
        else:
            messages.error(request, "Usuario o contrasena incorrecta")

    return render(request, 'users/login.html', {})

def salir(request):
    logout(request)
    messages.success(request, "Has cerrado sesión.")
    return redirect(login)

def registro(request):
    if request.user.is_authenticated:
        return redirect(index)
    
    #OBTENCION DE DATOS
    form = Regristo(request.POST or None) #aqui se almacenara el formulario si se hace la peticion
    if request.method == "POST" and form.is_valid(): #Si es post, es que enviaron el formulario
        
        usuario = form.save() #Guardamos el usuario
        if usuario:
            # Autenticar primero para que Django asigne el backend correcto
            usuario_autenticado = authenticate(
                request, 
                username=usuario.username, 
                password=form.cleaned_data['password']
            )
            if usuario_autenticado:
                lg(request, usuario_autenticado) #Login del nuevo usuario
                messages.success(request, f"Usuario creado exitosamente, bienvenido {usuario.username}")
                return redirect(index)
        
    return render(request, 'users/registro.html', {
        'form': form #es lo que se está mostrando en el HTML
    })