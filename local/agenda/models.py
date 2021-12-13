from django.db import models
from local.local.models import Local
from cliente.models import Cliente
# from codigo_qr.codigo import crear_qr
from .correo import sendCorreo
from django.db.models.signals import post_save
from django.core.files import File
import qrcode



class Hora(models.Model):
    id = models.AutoField(primary_key = True)
    hora = models.TimeField('Hora', auto_now_add = False, auto_now = False, blank = False, null = False)

    class Meta:
        verbose_name = 'Hora'
        verbose_name_plural = 'Horas'

    def __str__(self) -> str:
        return f'{self.id}'

class Agenda(models.Model):
    id = models.AutoField(primary_key = True)
    id_local = models.ForeignKey(Local, on_delete = models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    fecha = models.DateField('Fecha', auto_now_add = False, auto_now = False)
    id_hora = models.ForeignKey(Hora, on_delete = models.CASCADE, blank = False, null = False)
    codigo_qr = models.ImageField(upload_to = 'qr', blank = True, null = True)
    estado = models.BooleanField('estado', default = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = False, auto_now_add = True)
    fecha_actualizacion = models.DateField('fecha de actualización', auto_now_add = False, auto_now = True)

    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'

    def __str__(self) -> str:
        return f'{self.id}'

def crearCodigoQr(sender, instance, created, **kwargs):
    if created:
        data = {
            'local' : instance.id_local.nombre,
            'direccion' : instance.id_local.direccion,
            'cliente' : f'{instance.id_cliente.nombres} {instance.id_cliente.apellidos}',
            'contacto' : instance.id_cliente.email,
            'fecha' : instance.fecha,
            'hora' : instance.id_hora.hora,
            'reserva' : instance.id
        }
    
        img = qrcode.make(instance.id)
        img.save('qr.png', format = 'png')
        instance.codigo_qr.save('qr.png', File(open('qr.png','rb')), save = True)
        instance.save()

        sendCorreo(data, instance.codigo_qr.url)

post_save.connect(crearCodigoQr,sender = Agenda)