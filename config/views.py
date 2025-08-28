from django.http import HttpResponse
from django.shortcuts import render

#El dicionario(CONTEXT)son las variables a utlizar en el html
def saludo(request):
    return render(request, 'index.html', {
        "titulo": "Personas",
        "mensaje": "Ingreso de personas",
        "personas": [
            {'titulo':'Maria', 'edad':15, 'adulto':False},
            {'titulo':'Pablo', 'edad':20, 'adulto':True},
            {'titulo':'Jorge', 'edad':11, 'adulto':False},
            {'titulo':'Marta', 'edad':44, 'adulto':True},
        ]
    })