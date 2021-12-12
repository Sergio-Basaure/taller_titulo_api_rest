from django.db import models

class Usuario(models.Model):
    
    id = models.AutoField(primary_key = True)
    username = models.CharField('Usuario', max_length = 50, unique = True, blank = False, null = False)
    email = models.EmailField('Correo electrónico', max_length = 100, unique = True, blank = False, null = False)
    nombres = models.CharField('Nombres del usuario', max_length = 100, blank = False, null = False)
    apellidos = models.CharField('Apellidos del usuario', max_length = 100, blank = False, null = False)
    rut = models.CharField('Rut del usuario', max_length = 10, unique = True, blank = False, null = False)
    contacto = models.IntegerField('Contacto del usuario', blank = False, null = False)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    #objects = UsuarioManager()  #   Para usar este manager

    # USERNAME_FIELD = 'username' #   o email -> campo representativo del usuario
    # REQUIRED_FIELDS = ['email', 'nombres', 'apellidos', 'rut', 'contacto']
    

    class Meta:
        verbose_name = 'Usuario'
        # verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'
