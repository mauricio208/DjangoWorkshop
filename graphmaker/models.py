from django.db import models

# Create your models here.

class Account(models.Model):
    data = models.CharField(max_length=150)
    childs = models.ManyToManyField('Account')