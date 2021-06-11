from django.db import models
from django.contrib import admin
# Create your models here.

class Certificate(models.Model):
    c_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=245)
    type = models.CharField(max_length=245, choices=[('Student', 'Student'), ('Individual', 'Individual')])
    college = models.CharField(max_length=245)
    dept_name = models.CharField(max_length=245)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=245)
    email = models.CharField(max_length=245)
    phone = models.IntegerField()
    gender = models.CharField(max_length=50, choices=[('Male', 'Male'), ('Female', 'Female')])
    type = models.CharField(max_length=245, choices=[('Student', 'Student'), ('Individual', 'Individual')])
    card = models.FileField()
    dob = models.DateField()

    def __str__(self):
        return self.name