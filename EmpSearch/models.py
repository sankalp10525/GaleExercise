from django.db import models


# Create your models here.


class Project(models.Model):
    pname = models.CharField(max_length=100)
    pmanager = models.CharField(max_length=100)
    p_startdate = models.DateField()
    p_enddate = models.DateField()


    def __str__(self):
        return self.pname


class Employee(models.Model):
    efirstname = models.CharField(max_length=100)
    elastname = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.EmailField(max_length=100)
    phonenumber = models.CharField(max_length=12)
    designation = models.CharField(max_length=100)
    Project = models.ManyToManyField(Project)
    def __str__(self):
        return self.efirstname
