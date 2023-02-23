from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager


class Policeman(AbstractUser):
    username = None
    identification_number = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "identification_number"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
