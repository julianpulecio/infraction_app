from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from apps.vehicle.models import Vehicle
from apps.vehicle.validators import validate_plate_format


class VehicleSerializer(serializers.ModelSerializer):
    plate = serializers.CharField(validators=[
        validate_plate_format,
        UniqueValidator(queryset=Vehicle.objects.all())
    ])

    class Meta:
        model = Vehicle
        fields = '__all__'

class VehicleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['brand','color','person']
