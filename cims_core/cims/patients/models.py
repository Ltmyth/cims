from django.db import models

# Create your models here.
class Patient(models.Model):
    full_name = models.CharField(max_length=80)
    symptoms = models.CharField(max_length=200)
    diagnosis = models.CharField(max_length=200)
    time_of_visit = models.DateTimeField(auto_now=True)
