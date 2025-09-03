from django.contrib import admin

# Register your models here.
from .models import Product
admin.site.register(Product) #Añade la tabla al panel de admin django
