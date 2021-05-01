from django.db import models

# Create your models here.
opcion_usuario = [
	[0, "dueño"],
	[1, "veterinario"]
]
class Usuario(models.Model):
	Rut        = models.CharField(primary_key=True,max_length=10) 
	Nombre     = models.CharField(max_length=20,null=True) 
	Apellidop  = models.CharField(max_length=20,null=True)
	Direccion  = models.CharField(max_length=80,null=True) 
	Contraseña = models.CharField(max_length=40,null=True) 
	Email      = models.CharField(max_length=80,default='gmail') 
	Edad       = models.IntegerField(null=True,default=0)
	Tipo_usuario = models.IntegerField(choices=opcion_usuario)
	def __str__(self):
		return self.Nombre

class Pet(models.Model):
	Nombre = models.CharField(max_length=20)
	Tipo   = models.CharField(max_length=8)
	Amo    = models.ForeignKey(Usuario,null=False,blank=False,on_delete=models.PROTECT) 
	foto   = models.ImageField(upload_to='mascotas',null=True)
	def __str__(self):
		return self.Nombre
