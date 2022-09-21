from django.db import models

# Create your models here.
class Personnel(models.Model):
    fullname = models.CharField(max_length=80)
    designation = models.CharField(max_length=80)
    password = models.CharField(max_length=20)
