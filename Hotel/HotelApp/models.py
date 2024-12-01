from django.contrib.auth.hashers import check_password
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Usuario(models.Model):
    nombre = models.CharField(max_length=15,null=False)
    correo = models.EmailField(max_length=50,null= False)
    contraseña = models.CharField(max_length=80,null=False)
    Ciudad= models.CharField(max_length=30,default="N/A")
    rol = models.CharField(max_length=20, default="Cliente")
    
    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre']

    def check_password(self, raw_password):
        # Usa check_password para verificar la contraseña
        return check_password(raw_password, self.contraseña)
    

class Habitacion(models.Model):
    piso = models.IntegerField()
    nhabitacion = models.IntegerField()  
    Estado = models.BooleanField(default=False)  


class Reservas(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    correo = models.TextField(null=False)
    contraseña = models.CharField(max_length=50, null=False)
    piso = models.IntegerField()
    nhabitacion = models.IntegerField()  
    # propietario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Un hotel tiene un propietario
