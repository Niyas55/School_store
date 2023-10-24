from typing import Set

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



class Store(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateField(default=True)
    age=models.IntegerField(blank=True)
    gender = models.CharField(max_length=250)
    ph = PhoneNumberField(max_length=10)
    email = models.EmailField(max_length=250)
    address = models.TextField(max_length=250)
    dept =models.CharField(max_length=250)
    course = models.CharField(max_length=250)
    purpose = models.CharField(max_length=250)
    material = models.CharField(max_length=250)

    def __str__(self):
        return self.name
