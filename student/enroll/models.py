from django.db import models

# Create your models here.

class StudentInfo(models.Model):
    name=models.CharField(max_length=50)
    roll=models.IntegerField()
    email=models.EmailField( max_length=254)