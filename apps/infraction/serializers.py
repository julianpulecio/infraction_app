from django.core.exceptions import ValidationError
from rest_framework import serializers

from apps.infraction.models import Infraction
from apps.infraction.validators import validate_placa_patente
from apps.policeman.models import Policeman
from apps.policeman.serializers import PolicemanReadSerializer
from apps.vehicle.models import Vehicle
from apps.vehicle.serializers import VehicleSerializer
from apps.vehicle.validators import validate_plate_format


class InfractionSerializer(serializers.ModelSerializer):
    placa_patente = serializers.CharField(validators=[
        validate_plate_format,
        validate_placa_patente,
    ])
    timestamp = serializers.DateTimeField()
    comentarios = serializers.CharField()

    class Meta:
        model = Infraction
        fields = ['placa_patente', 'timestamp', 'comentarios']

    def custom_create(self, validated_data, policeman):
        vehicle = Vehicle.objects.filter(plate=validated_data.get('placa_patente')).first()
        return Infraction.objects.create(
            vehicle=vehicle,
            policeman=policeman,
            timestamp=validated_data.get('timestamp'),
            comments=validated_data.get('comentarios')
        )


class InfractionReadSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(Vehicle)
    policeman = PolicemanReadSerializer(Policeman)

    class Meta:
        model = Infraction
        fields = '__all__'


class InfractionVehiclesSerializer(serializers.ModelSerializer):
    infractions = InfractionReadSerializer(Infraction, many=True)
    class Meta:
        model = Vehicle
        fields = ['infractions']
