from django.db import models

# Create your models here.

class Blog(models.Model):
    titulo = models.CharField(max_length=200, null=False, blank=False)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='media/blog')

    def __str__(self):
        return self.titulo

