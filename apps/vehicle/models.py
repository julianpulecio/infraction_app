from django.db import models
from apps.person.models import Person
from apps.vehicle.validators import validate_plate_format


class Vehicle(models.Model):
    plate = models.CharField(max_length=6)
    brand = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='vehicles')