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