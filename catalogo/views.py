from django.db.models import DecimalField, ExpressionWrapper, F, Sum
from django.shortcuts import render
from django.views.generic import ListView

from .models import Producto


def home(request):
    productos = [
        {
            'nombre': 'Laptop Lenovo ThinkPad',
            'categoria': 'Computadoras',
            'precio': 3500,
            'stock': 8,
            'descripcion': 'Equipo ideal para clases, oficina y desarrollo web.',
            'etiqueta': 'Destacado',
        },
        {
            'nombre': 'Mouse Logitech M90',
            'categoria': 'Accesorios',
            'precio': 80,
            'stock': 35,
            'descripcion': 'Mouse optico USB para trabajo diario.',
            'etiqueta': 'Disponible',
        },
        {
            'nombre': 'Teclado Redragon Kumara',
            'categoria': 'Accesorios',
            'precio': 120,
            'stock': 18,
            'descripcion': 'Teclado mecanico compacto para productividad y gaming.',
            'etiqueta': 'Popular',
        },
        {
            'nombre': 'Monitor LG 24 pulgadas',
            'categoria': 'Pantallas',
            'precio': 640,
            'stock': 12,
            'descripcion': 'Monitor Full HD para estudio, diseno y oficina.',
            'etiqueta': 'Nuevo',
        },
        {
            'nombre': 'Audifonos HyperX Cloud',
            'categoria': 'Audio',
            'precio': 280,
            'stock': 15,
            'descripcion': 'Audifonos con microfono para reuniones y entretenimiento.',
            'etiqueta': 'Oferta',
        },
        {
            'nombre': 'Impresora Epson EcoTank',
            'categoria': 'Impresion',
            'precio': 980,
            'stock': 5,
            'descripcion': 'Impresora multifuncional para alto volumen de trabajo.',
            'etiqueta': 'Bajo stock',
        },
    ]

    resumen = {
        'total_productos': len(productos),
        'categorias': len({producto['categoria'] for producto in productos}),
        'stock_total': sum(producto['stock'] for producto in productos),
    }

    return render(
        request,
        'catalogo.html',
        {
            'productos': productos,
            'resumen': resumen,
        },
    )


class ProductoListView(ListView):
    model = Producto
    template_name = 'productos.html'
    context_object_name = 'productos'
    ordering = ['-destacado', 'nombre']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        productos = self.object_list
        valor_inventario = ExpressionWrapper(
            F('precio') * F('stock'),
            output_field=DecimalField(max_digits=12, decimal_places=2),
        )

        context['resumen'] = productos.aggregate(
            stock_total=Sum('stock'),
            valor_total=Sum(valor_inventario),
        )
        context['total_productos'] = productos.count()
        context['admin_url'] = 'http://127.0.0.1:8000/admin'
        return context
