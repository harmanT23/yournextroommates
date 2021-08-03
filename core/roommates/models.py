from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

# model for listing
class Listing(models.Model):
    pass

# model for user - Staff, Poster, roomie
class User(AbstractUser):
    pass