from .models import QrAgenda
from django.core.files import File
import qrcode
from .correo import sendCorreo

def crear_qr(data):
    id = data['reserva']
    url = f'agenda/{id}'
    img = qrcode.make(data = url)
    img.save('qr.png', format = 'png')
    q = QrAgenda()
    q.codigo_qr.save('qr.png', File(open('qr.png','rb')), save = True)
    q.save()
    sendCorreo(data = data, qr = q.codigo_qr)

