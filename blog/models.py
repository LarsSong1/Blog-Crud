from django.db import models
from django.utils import timezone

# Create your models here.

class Blog(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    now = timezone.now()
    imagen = models.ImageField()
    categoria = models.CharField(max_length=30, default='')
    subtitulo = models.CharField(max_length=25, default='')
    titulo = models.CharField(max_length=40, default='')
    autor = models.CharField(max_length=40, default="Anonimo")
    # comentarios = models.AutoField(primary_key=True)
    fechaPublicacion = models.DateField(auto_now=True)
    informacion = models.TextField()

    class Meta:
        verbose_name = 'Blogs'
        verbose_name_plural = 'Publicaciones'

    def __str__(self):
        return self.titulo



