# models.py

from django.db import models

class Employee(models.Model):
    employeeName = models.CharField(max_length=255)
    employeeId = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=20)
