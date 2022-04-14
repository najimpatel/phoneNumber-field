from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Student(models.Model):
    name = models.CharField(max_length=20)
    phone_number = PhoneNumberField()
    roll = models.IntegerField()
    city = models.CharField(max_length=20)

