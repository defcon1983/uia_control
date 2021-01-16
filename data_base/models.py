from django.db import models

# Create your models here.


class Profesor(models.Model):
    email = models.EmailField(max_length=256, null=False,blank=False)


class Alumno(models.Model):
    email = models.EmailField(max_length=256, null=False, blank=False)
