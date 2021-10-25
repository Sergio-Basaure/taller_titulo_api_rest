from django.db import models
from ..categoria.models import CategoriaServicio


class Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length = 50, blank=False,null=False,unique=True)
    descripcion = models.TextField('Descripción', max_length = 300, blank = False, null = False)
    id_categoria = models.ForeignKey(CategoriaServicio, on_delete=models.CASCADE)
    estado = models.BooleanField('Estado', default = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = False, auto_now_add = True)
    fecha_actualizacion = models.DateField('fecha de actualización', auto_now_add = False, auto_now = True)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self) -> str:
        return self.nombre