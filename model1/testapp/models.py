from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=70)
    marks=models.FloatField()

