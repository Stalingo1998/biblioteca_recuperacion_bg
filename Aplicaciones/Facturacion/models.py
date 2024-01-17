import os
from django.db import models

# Create your models here.
from django.db import models

class GeneroLiterario(models.Model):
    id_bg = models.AutoField(primary_key=True)
    nombre_bg = models.CharField(max_length=150)
    descripcion_bg = models.TextField()
    fotografia_referencia = models.FileField(upload_to='genero', null=True, blank=True)

    def __str__(self):
        return self.nombre_bg


class Profesion(models.Model):
    id_bg = models.AutoField(primary_key=True)
    nombre_bg = models.CharField(max_length=150)
    descripcion_bg = models.TextField()

    def __str__(self):
        return self.nombre_bg


class Autor(models.Model):
    id_bg = models.AutoField(primary_key=True)
    apellido_bg = models.CharField(max_length=150)
    nombre_bg = models.CharField(max_length=150)
    edad_bg = models.IntegerField()
    fotografia_portada = models.FileField(upload_to='autor', null=True, blank=True)

    profesion_bg = models.ForeignKey(Profesion, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f"{self.apellido_bg}, {self.nombre_bg}"


class Libro(models.Model):
    id_bg = models.AutoField(primary_key=True)
    titulo_bg = models.CharField(max_length=150)
    editorial_bg = models.CharField(max_length=150)
    fecha_publicacion_bg = models.DateField()
    fotografia_portada = models.FileField(upload_to='portada', null=True, blank=True)

    genero_bg = models.ForeignKey(GeneroLiterario, on_delete=models.PROTECT, null=True, blank=True)
    autor_bg = models.ForeignKey(Autor, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.titulo_bg
