from django.db import models
from ..categoria.models import CategoriaProducto

class Producto(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre', max_length = 100, blank = False, null = False)
    marca = models.CharField('Marca', max_length = 100, blank = False, null = False)
    descripcion = models.TextField('Descripcion', max_length = 300, blank = False, null = False)
    id_categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    estado = models.BooleanField('Estado', default = True)
    stock = models.IntegerField('Stock', blank = False, null = False)
    precio = models.IntegerField(blank = False, null = False)
    imagen = models.URLField(max_length = 250, blank = False, null = False)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = False, auto_now_add = True)
    fecha_actualizacion = models.DateField('fecha de actualización', auto_now_add = False, auto_now = True)


    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self) -> str:
        return f'{self.nombre}'