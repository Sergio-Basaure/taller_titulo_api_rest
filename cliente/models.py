from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

class Cliente(AbstractBaseUser):
    id = models.AutoField(primary_key = True)
    rut = models.CharField('Rut', max_length = 10, blank = False, null = False, unique = True)
    nombres = models.CharField('Nombres', max_length = 100, blank = False, null = False)
    apellidos = models.CharField('Apellidos', max_length = 100, blank = False, null = False)
    email = models.EmailField(blank = False, null = False, unique = True)
    password = models.CharField('Password', max_length = 100, blank = False, null = False)
    contacto = models.IntegerField('Contacto', blank=False,null=False)
    estado = models.BooleanField('Estado', default = True)
    last_login = models.DateTimeField('last login',auto_now=True, blank=True, null=True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = False, auto_now_add = True)
    fecha_actualizacion = models.DateField('fecha de actualización', auto_now_add = False, auto_now = True)

    objects = UserManager()


    USERNAME_FIELD = 'email' #   o email -> campo representativo del usuario
    REQUIRED_FIELDS = ['nombres', 'apellidos', 'rut', 'contacto']

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f'{self.id}'