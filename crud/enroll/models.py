from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=70,null=True)
    lastname = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
