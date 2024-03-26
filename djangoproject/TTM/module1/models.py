

from django.db import models
from .forms import forms

class Register(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=100)
    phonenumber=models.PositiveBigIntegerField()
    class Meta:
        db_table="Register"

class contactus(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    phonenumber = models.PositiveBigIntegerField()
    comment = models.CharField(max_length=100)
    feedback = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    class Meta:
        db_table="contactus"



