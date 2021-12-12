from django.db import models

class TipoReclamo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('nombre',max_length=50,blank=False,null=False,unique=True)
    estado = models.BooleanField('Estado', default = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = False, auto_now_add = True)
    fecha_actualizacion = models.DateField('fecha de actualización', auto_now_add = False, auto_now = True)

    class Meta:
        verbose_name = 'Categoria de reclamo'
        verbose_name_plural = 'Categorias de reclamos'

    def __str__(self) -> str:
        return self.nombre