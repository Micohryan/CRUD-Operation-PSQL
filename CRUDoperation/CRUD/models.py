from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class EmpModel(models.Model):
    empname = models.CharField(max_length = 1000)
    email = models.CharField(max_length = 1000)
    occupation= models.CharField(max_length = 1000)
    salary = models.IntegerField()
    gender = models.CharField(max_length = 1000)
    class Meta:
        db_table = 'employee'
