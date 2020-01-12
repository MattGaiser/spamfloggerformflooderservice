from django.db import models

# Create your models here.
class CodesForForms(models.Model):
    url = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)