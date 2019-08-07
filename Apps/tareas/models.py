from django.db import models
from Apps.user.models import User
# Create your models here.


class tarea(models.Model):

	Status = models.BooleanField(default=False)
	Creado = models.DateTimeField(auto_now_add=True)
	Modificado =models.DateTimeField(auto_now=True)
	Titulo = models.CharField(max_length=100)
	Description = models.TextField(max_length=200)
	Fecha = models.DateField()
	Hora = models.TimeField()
	user = models.ForeignKey(User, related_name="user", null=False, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.Titulo

	# @classmethod
	def tarea_muestra(self):
		de = self.Description
		return de[0:20]

	def status(self):
		return self.Status