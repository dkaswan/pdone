from pyexpat import model
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    phone = models.CharField(max_length=13)
    message = models.TextField()
    date = models.DateField()