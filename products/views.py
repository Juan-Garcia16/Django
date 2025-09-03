from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product

# Create your views here.
class ProductListView(ListView):
    template_name = 'index.html' #plantilla donde se renderiza la lista de productos
    queryset = Product.objects.all() #Todas las instancias de productos
    
    # El contexto es el diccionario de variables que se pasa a la plantilla
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mensaje'] = 'Lista de productos' # Este es el mensaje que se mostrará en la plantilla, se pueden añadir más variables aquí
        return context