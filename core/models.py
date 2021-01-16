from django.db import models

# Create your models here.

class Licenciaturas(models.Model):
    titulo = models.CharField(max_length = 150)
    descripcion = models.TextField()
    
class Maestrias(models.Model):
    titulo = models.CharField(max_length = 150)
    descripcion = models.TextField() 

class QuienesSomos(models.Model):
    contenido = models.TextField()
    
class Reglamento(models.Model):
    reglamento = models.TextField()
    
class campus(models.Model):
    nombre = models.CharField(max_length = 150)
    imagen = models.ImageField(upload_to='media/campus')

class contactanos(models.Model):
    nombre = models.CharField(max_length = 150)
    email = models.EmailField(max_length=256)
    telefono = models.CharField(max_length = 150)
    mensaje = models.CharField(max_length = 3000)
