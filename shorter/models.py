from django.db import models

class Main_db(models.Model):
    shorturl = models.CharField(max_length=50)
    longurl = models.CharField(max_length=200)

class user_db(models.Model):
    login = models.CharField(max_length=16)
    password = models.CharField(max_length=16)

# Create your models here.
