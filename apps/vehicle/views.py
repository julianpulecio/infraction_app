from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ViewSet

from apps.vehicle.serializers import VehicleSerializer


class VehicleViewSet(ViewSet):
    def list(self, request):
        pass

    @swagger_auto_schema(request_body=VehicleSerializer)
    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    @swagger_auto_schema(request_body=VehicleSerializer)
    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass