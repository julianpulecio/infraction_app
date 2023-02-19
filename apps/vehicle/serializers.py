from rest_framework import serializers
from apps.vehicle.models import Vehicle
from apps.vehicle.validators import validate_plate_format


class VehicleSerializer(serializers.ModelSerializer):
    plate = serializers.CharField(validators=[validate_plate_format])

    class Meta:
        model = Vehicle
        fields = '__all__'
