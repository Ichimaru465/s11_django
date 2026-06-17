from django.contrib import admin

from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'categoria',
        'precio',
        'stock',
        'proveedor',
        'destacado',
        'fecha_registro',
    )
    list_filter = ('categoria', 'destacado', 'fecha_registro')
    search_fields = ('nombre', 'categoria', 'proveedor')
    ordering = ('nombre',)
    list_editable = ('precio', 'stock', 'destacado')