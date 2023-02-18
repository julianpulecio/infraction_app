from django.db import models
from apps.vehicle.models import Vehicle


class Infraction(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='infractions')
    timestamp = models.DateTimeField(auto_now_add=True)
