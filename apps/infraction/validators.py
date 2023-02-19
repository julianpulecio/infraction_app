from rest_framework.exceptions import ValidationError
from apps.vehicle.models import Vehicle


def validate_placa_patente(value):
    if not Vehicle.objects.filter(plate=value):
        raise ValidationError('vehicle not found')