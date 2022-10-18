from tabnanny import verbose
from django.db import models


# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length = 20, verbose_name = 'students name')
    last_name = models.CharField(max_length = 20, verbose_name = 'stidents last name')
    age = models.IntegerField()
    gender = models.CharField(max_length = 20, verbose_name = 'sex')
    departament = models.CharField(max_length = 20, verbose_name = 'department')