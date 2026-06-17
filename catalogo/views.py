from django.shortcuts import render

def home(request):

    productos = [
        {'nombre':'Laptop', 'precio':3500},
        {'nombre':'Mouse', 'precio':80},
        {'nombre':'Teclado', 'precio':120},
    ]

    return render(request,
                  'catalogo/catalogo.html',
                  {'productos': productos})

from django.views.generic import ListView
from .models import Producto

class ProductoListView(ListView):
    model = Producto
    template_name = 'catalogo/productos.html'
    context_object_name = 'productos'
