from django.db import models
from django.urls import reverse

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
	Email      = models.CharField(max_length=80) 
	Edad       = models.IntegerField(null=True)
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

class Comenta(models.Model):
	usu = models.ForeignKey(Usuario,null=False,blank=False,on_delete=models.PROTECT)
	id_comentario = models.AutoField(primary_key=True)
	descripcion = models.CharField(max_length=50,null=True)
	comentario = models.TextField(max_length=1000,null=True)
	def __str__(self):
		return str(self.id_comentario)



