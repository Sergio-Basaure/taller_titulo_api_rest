from django.db import models

class Local(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre del local', max_length = 100, blank = False, null = False, unique = True)
    direccion = models.CharField('Dirección del local', max_length = 200, blank = False, null = False, unique = True)
    contacto = models.IntegerField('Conatcto', blank = False, null = False)
    estado = models.BooleanField('Estado', default = True, null = False)
    imagen = models.URLField(max_length = 255, blank = False)
    aforo_maximo = models.PositiveIntegerField('Aforo Maximo', blank = False, null = False)
    aforo_actual = models.PositiveIntegerField('Aforo actual', blank = False, null = False, default = 0)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = False, auto_now_add = True)
    fecha_actualizacion = models.DateField('fecha de actualización', auto_now_add = False, auto_now = True)

    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = 'Locales'

    def __str__(self):
        return f'{self.id}'