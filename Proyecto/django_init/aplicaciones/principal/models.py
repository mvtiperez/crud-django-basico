from django.db import models

"""Cada uno de estos modelos es una tabla en la DB"""
class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=100, unique=True)
    apellido= models.CharField(max_length=100, unique=True)
    correo= models.EmailField(max_length=200, unique=True)

    def __str__(self):
        return self.nombre
