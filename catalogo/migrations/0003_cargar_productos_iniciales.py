from decimal import Decimal

from django.db import migrations


PRODUCTOS_INICIALES = [
    {
        'nombre': 'Laptop Lenovo ThinkPad',
        'descripcion': 'Equipo ideal para clases, oficina y desarrollo web.',
        'categoria': 'Computadoras',
        'precio': Decimal('3500.00'),
        'stock': 8,
        'proveedor': 'Lenovo Peru',
        'destacado': True,
    },
    {
        'nombre': 'Mouse Logitech M90',
        'descripcion': 'Mouse optico USB para trabajo diario.',
        'categoria': 'Accesorios',
        'precio': Decimal('80.00'),
        'stock': 35,
        'proveedor': 'Logitech',
        'destacado': False,
    },
    {
        'nombre': 'Teclado Redragon Kumara',
        'descripcion': 'Teclado mecanico compacto para productividad y gaming.',
        'categoria': 'Accesorios',
        'precio': Decimal('120.00'),
        'stock': 18,
        'proveedor': 'Redragon',
        'destacado': True,
    },
    {
        'nombre': 'Monitor LG 24 pulgadas',
        'descripcion': 'Monitor Full HD para estudio, diseno y oficina.',
        'categoria': 'Pantallas',
        'precio': Decimal('640.00'),
        'stock': 12,
        'proveedor': 'LG',
        'destacado': False,
    },
    {
        'nombre': 'Audifonos HyperX Cloud',
        'descripcion': 'Audifonos con microfono para reuniones y entretenimiento.',
        'categoria': 'Audio',
        'precio': Decimal('280.00'),
        'stock': 15,
        'proveedor': 'HyperX',
        'destacado': False,
    },
    {
        'nombre': 'Impresora Epson EcoTank',
        'descripcion': 'Impresora multifuncional para alto volumen de trabajo.',
        'categoria': 'Impresion',
        'precio': Decimal('980.00'),
        'stock': 5,
        'proveedor': 'Epson',
        'destacado': False,
    },
]


def cargar_productos(apps, schema_editor):
    Producto = apps.get_model('catalogo', 'Producto')

    for datos in PRODUCTOS_INICIALES:
        Producto.objects.get_or_create(
            nombre=datos['nombre'],
            defaults=datos,
        )


def eliminar_productos(apps, schema_editor):
    Producto = apps.get_model('catalogo', 'Producto')
    nombres = [producto['nombre'] for producto in PRODUCTOS_INICIALES]
    Producto.objects.filter(nombre__in=nombres).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_producto_categoria_producto_descripcion_and_more'),
    ]

    operations = [
        migrations.RunPython(cargar_productos, eliminar_productos),
    ]
