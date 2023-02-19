from django.db import models
from apps.policeman.models import Policeman
from apps.vehicle.models import Vehicle


class Infraction(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='infractions')
    policeman = models.ForeignKey(Policeman, on_delete=models.CASCADE, related_name='infractions')
    timestamp = models.DateTimeField(auto_now_add=False)
    comments = models.CharField(max_length=255)
