from django.http import HttpResponse
from django.shortcuts import render

#El dicionario(CONTEXT)son las variables a utlizar en el html
def saludo(request):
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

    if request.method == "POST":
        username = request.POST.get("username") #El post es un diccionario, recibimos la clave
        password = request.POST.get("password") 
        print(f"Username: {username}, Password: {password}")
    return render(request, 'users/login.html', {})