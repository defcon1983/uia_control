from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Carrera(models.Model):
  titulo = models.CharField(max_length=150, verbose_name="Título")
  duracion_carrera = models.FloatField()
  descripcion = models.TextField(help_text="Descripción corta")
  imagen = models.ImageField(upload_to='img/')
  video = models.FileField(upload_to='videos/', null=True, verbose_name="")
  elegir_semestre = [
    (1, 'primero'),
    (2, 'segundo'),
    (3, 'tercero' ),
    (4, 'cuarto'),
    (5, 'quinto'),
    (6, 'sexto'),
    (7, 'septimo'),
    (8, 'optavo'),
    (9, 'noveno')
  ]
  semestre = models.IntegerField(null=False, blank=False, choices=elegir_semestre, default=1)

  class Meta:
    ordering = ['titulo']
  
  def __str__(self):
    return self.titulo



class Materia(models.Model):
  titulo = models.CharField(max_length=200)
  parcial_1 = models.FloatField(null=False,blank=False, default=0)
  parcial_2 = models.FloatField(null=False,blank=False, default=0)
  parcial_3 = models.FloatField(null=False,blank=False, default=0)
  maestro_asignado = models.CharField(max_length=200)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

  def __str__(self):
    return self.titulo








#class Carrera(models.Model):
#  titulo = models.CharField(max_length=150, verbose_name="Título")
#  duracion_carrera = models.FloatField()
#  descripcion = models.TextField(help_text="Descripción corta")
#  imagen = models.ImageField(upload_to='img/')
#  video = models.FileField(upload_to='videos/', null=True, verbose_name="")
#
#  class Meta:
#    ordering = ['titulo']
#  
#  def __str__(self):
#    return self.titulo
#
#class Materia(models.Model):
#  titulo = models.CharField(max_length=200)
#  maestro_asignado = models.CharField(max_length=200)
#
#  def __str__(self):
#    return self.titulo
#
#
#class Calificacion(models.Model):
#  parcial_1 = models.FloatField(null=False,blank=False, default=0)
#  parcial_2 = models.FloatField(null=False,blank=False, default=0)
#  parcial_3 = models.FloatField(null=False,blank=False, default=0)
#  elegir_semestre = [
#    (1, 'primero'),
#    (2, 'segundo'),
#    (3, 'tercero' ),
#    (4, 'cuarto'),
#    (5, 'quinto'),
#    (6, 'sexto'),
#    (7, 'septimo'),
#    (8, 'optavo'),
#    (9, 'noveno')
#  ]
#  semestre = models.IntegerField(null=False, blank=False, choices=elegir_semestre, default=1)
#  carrera = models.OneToOneField(Carrera, on_delete=models.CASCADE)
#  materia = models.OneToOneField(Materia, on_delete=models.CASCADE)
#  user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#
#  def natural_key(self):
#    return (self.semestre)
#
#  def __str__(self):
#    suma = self.parcial_1 + self.parcial_2 + self.parcial_3
#    self.promedio = suma/3
#    txt = "alumno: {0} | semestre: {1} | materia: {2} | promedio: {3}"
#    return txt.format(self.user, self.semestre, self.materia, self.promedio)
#