from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from apps.vehicle.models import Vehicle
from apps.vehicle.serializers import VehicleSerializer, VehicleUpdateSerializer


class VehicleViewSet(ViewSet):
    def list(self, request):
        queryset = Vehicle.objects.all()
        policemen_serialized = VehicleSerializer(queryset, many=True)
        return Response(policemen_serialized.data)

    @swagger_auto_schema(request_body=VehicleSerializer)
    def create(self, request):
        serializer = VehicleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        vehicle = serializer.create(serializer.validated_data)
        vehicle_serialized = VehicleSerializer(vehicle)
        return Response(vehicle_serialized.data)

    def retrieve(self, request, plate=None):
        queryset = Vehicle.objects.all()
        policeman = get_object_or_404(queryset, plate=plate)
        policeman_serialized = VehicleSerializer(policeman)
        return Response(policeman_serialized.data)

    @swagger_auto_schema(request_body=VehicleUpdateSerializer)
    def update(self, request, plate=None):
        queryset = Vehicle.objects.all()
        vehicle = get_object_or_404(queryset, plate=plate)
        serializer = VehicleUpdateSerializer(vehicle, data=request.data)
        serializer.is_valid(raise_exception=True)
        vehicle_updated = serializer.update(vehicle, serializer.validated_data)
        vehicle_updated_serialized = VehicleSerializer(vehicle_updated)
        return Response(vehicle_updated_serialized.data)

    def destroy(self, request, plate=None):
        queryset = Vehicle.objects.all()
        vehicle = get_object_or_404(queryset, plate=plate)
        vehicle.delete()
        return Response({'response': 'the vehicle was deleted successfully'})