from django.db import models

class menu (models.Model):
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=30)

# Create your models here.
