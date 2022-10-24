from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#usuario em geral
class User(models.Model):
    
    nome = models.CharField(max_length=256)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length=50)

     
    def __str__(self) -> str:
        return self.nome

class UserRant(models.Model):
    
    username = models.CharField(max_length=256)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length=50)
    nomeRant = models.CharField(max_length=256)
    endereco = models.CharField(max_length=256)
    horarioInicio = models.TimeField()
    horarioFinal = models.TimeField()
    tipo = models.CharField(max_length=256)
    
    
    def __str__(self) -> str:
        return self.nomeRant