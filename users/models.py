from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=12)
    country_code = models.CharField(max_length=12)
