from django.db import models
from django.db.models.fields import EmailField

# Create your models here.

class UserCredential(models.Model):
    email = EmailField()
    password = models.CharField(max_length=25)
    role = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name