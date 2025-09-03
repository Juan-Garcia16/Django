from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product
from django.views.generic.detail import DetailView

# Create your views here.
class ProductListView(ListView):
    template_name = 'index.html' #plantilla donde se renderiza la lista de productos
    queryset = Product.objects.all() #Todas las instancias de productos
    
    # El contexto es el diccionario de variables que se pasa a la plantilla
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mensaje'] = 'Lista de productos' # Este es el mensaje que se mostrará en la plantilla, se pueden añadir más variables aquí
        return context
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mensaje'] = 'Detalle del producto'
        return context
    
    
    #LO QUE HACE INTERNAMENTE
    # def get_queryset(self):
        
    #     queryset = Product.objects.get(id=self.kwargs['pk']) # Obtener el producto por su ID(Primary key)
    #     return queryset