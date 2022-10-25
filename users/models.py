from django.db import models
# Create your models here.


class UserRant(models.Model):
    username = models.CharField(max_length=256)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length=50)
    nomeRant = models.CharField(max_length=256)
    endereco = models.CharField(max_length=256)
    horarioInicio = models.TimeField()
    horarioFinal = models.TimeField()
    tipo = models.CharField(max_length=256)
    
