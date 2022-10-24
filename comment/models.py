from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    data =  models.DateTimeField(max_length=256)
    content = models.TextField(max_length=350)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.content