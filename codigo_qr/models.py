from django.db import models

class QrAgenda(models.Model):
    id = models.AutoField(primary_key=True)
    codigo_qr = models.ImageField(upload_to = 'qr')
    estado = models.BooleanField('estado', default = True)

    class Meta:
        verbose_name = 'Qr'
        verbose_name_plural = 'Qrs'
    
    def __str__(self) -> str:
        return f'{self.id}'