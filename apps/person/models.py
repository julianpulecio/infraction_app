from django.db import models


class Person(models.Model):
    email = models.EmailField(max_length=255)
    name = models.CharField(max_length=255)
