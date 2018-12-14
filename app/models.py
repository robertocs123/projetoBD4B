from django.db import models
from django.contrib.auth.models import User


class Tipo (models.Model):
	tipo = models.CharField(max_length = 20, unique=True)
	palavras_chaves = models.TextField(null=True, default='')
	def __str__ (self):
		return self.tipo

class Post (models.Model):
	id_publicacao = models.CharField(max_length=900000000000000, default='', null=True)
	mensagem = models.TextField()
	user = models.ForeignKey(User, on_delete = models.CASCADE, null= True)
	tipo = models.ManyToManyField(Tipo)
	data = models.DateField(null = True)