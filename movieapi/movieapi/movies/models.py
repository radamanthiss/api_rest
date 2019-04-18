from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Movie(models.Model):
	"""docstring for Movie"""
	titulo = models.CharField(max_length=255, null=False)
	genero = models.CharField(max_length=255, null=False)
	calificacion = models.IntegerField(default=0)
	fecha_lanzamiento = models.DateField()

	def __str__(self):
		return self.titulo

	

	

		