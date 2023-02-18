from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ViewSet

from apps.policeman.serializers import PolicemanSerializer


class PolicemanViewSet(ViewSet):
    def list(self, request):
        pass

    @swagger_auto_schema(request_body=PolicemanSerializer)
    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    @swagger_auto_schema(request_body=PolicemanSerializer)
    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass