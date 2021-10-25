from django.db import models
from ..local.models import Local
from ..categoria.models import TipoReclamo
from usuario.models import Usuario

class Reclamos(models.Model):
    id = models.AutoField(primary_key = True)
    id_tipo = models.ForeignKey(TipoReclamo, on_delete = models.CASCADE, blank = False, null = False)
    id_local = models.ForeignKey(Local, on_delete = models.CASCADE, blank = False, null = False)
    descripcion = models.TextField('Descripción', max_length = 300, blank = False, null = False)
    estado = models.BooleanField('Estado', default = True)
    asignado = models.BooleanField('Asignado', default = False)
    personal_asignado = models.ForeignKey(Usuario, on_delete = models.CASCADE, blank=True, null=True)
    descripcion_personal = models.TextField('Descripción del personal', max_length = 300, blank = True, null = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = False, auto_now_add = True)
    fecha_actualizacion = models.DateField('fecha de actualización', auto_now_add = False, auto_now = True)

    class Meta:
        verbose_name = 'Reaclamo y Sugerencia'
        verbose_name_plural = 'Reaclamos y Sugerencias'

    def __str__(self) -> str:
        return f'{self.id_tipo}'
