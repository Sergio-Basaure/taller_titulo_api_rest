from django.db import models

class CategoriaProducto(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre', max_length = 50,blank = False, null = False, unique = True)
    estado = models.BooleanField('Estado', default = True)
    imagen = models.URLField(max_length = 250, blank = False, null = False)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = False, auto_now_add = True)
    fecha_actualizacion = models.DateField('fecha de actualización', auto_now_add = False, auto_now = True)

    class Meta:
        verbose_name = 'Categoria Producto'
        verbose_name_plural = 'Categorias Productos'

    def __str__(self) -> str:
        return f'{self.id}'