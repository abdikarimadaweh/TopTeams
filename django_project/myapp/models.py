from django.db import models

# Create your models here.

class Player(models.Model):
    team = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    number = models.IntegerField()
    position = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    img = models.CharField(max_length=200)