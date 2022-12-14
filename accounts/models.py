from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    watchlist = models.CharField(max_length=5000, null=True)
    username = None

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []