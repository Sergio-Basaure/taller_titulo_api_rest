from django.db import models
from ..categoria.models import CategoriaProducto

class Producto(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre', max_length = 100, blank = False, null = False, unique = True)
    marca = models.CharField('Marca', max_length = 100, blank = False, null = False)
    descripcion = models.TextField('Descripcion', max_length = 300, blank = False, null = False)
    id_categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    estado = models.BooleanField('Estado', default = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add = False)
    fecha_actualizacion = models.DateField('fecha de actualización', auto_now_add = True, auto_now = False)


    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self) -> str:
        return f'{self.nombre}'