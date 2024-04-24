from django.db import models

# Create your models here.
class PuneJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=10)
    title = models.CharField(max_length=15)
    address = models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
class HydJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=10)
    title = models.CharField(max_length=15)
    address = models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
class BegrJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=10)
    title = models.CharField(max_length=15)
    address = models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
