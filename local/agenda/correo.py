from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings



def sendCorreo(data, qr):
    template = get_template('correo.html')
    contex = {
        'data' : data,
        'qr' : qr
    }
    content = template.render(contex)
    email = EmailMultiAlternatives(
        subject = 'titulo',
        from_email = settings.EMAIL_HOST_USER,
        to = [data['contacto']],
    )
    email.attach_alternative(content, 'text/html')
    email.send()