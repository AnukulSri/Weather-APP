from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=50)
    roll = models.CharField(max_length=10)
    email = models.EmailField()
    mob = models.CharField(max_length=15)
    pwd = models.CharField(max_length=25)
