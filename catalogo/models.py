from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, default='')
    categoria = models.CharField(max_length=60, default='General')
    precio = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    stock = models.PositiveIntegerField(default=0)
    proveedor = models.CharField(max_length=100, blank=True, default='')
    destacado = models.BooleanField(default=False)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre