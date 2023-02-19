from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from apps.vehicle.serializers import VehicleSerializer


class VehicleViewSet(ViewSet):
    def list(self, request):
        pass

    @swagger_auto_schema(request_body=VehicleSerializer)
    def create(self, request):
        serializer = VehicleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        vehicle = serializer.create(serializer.validated_data)
        vehicle_serialized = VehicleSerializer(vehicle)
        return Response(vehicle_serialized.data)

    def retrieve(self, request, pk=None):
        pass

    @swagger_auto_schema(request_body=VehicleSerializer)
    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass