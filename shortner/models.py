from django.db import models

# Create your models here.
class UniformResourceLocator(models.Model):
    linkAddress = models.CharField(max_length=10000)
    uuidCodeFormat = models.CharField(max_length=10)