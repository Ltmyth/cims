from django.db import models

# Create your models here.
class Usaz(models.Model):
    user_ID = models.CharField(max_length=10)
    user_name = models.CharField(max_length=20)
    sign_in_time = models.DateTimeField(auto_now=True)
