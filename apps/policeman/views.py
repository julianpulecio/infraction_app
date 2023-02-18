from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from apps.policeman.models import Policeman
from apps.policeman.serializers import PolicemanWriteSerializer, PolicemanReadSerializer


class PolicemanViewSet(ViewSet):
    def list(self, request):
        queryset = Policeman.objects.all()
        policemen_serialized = PolicemanReadSerializer(queryset, many=True)
        return Response(policemen_serialized.data)

    @swagger_auto_schema(request_body=PolicemanWriteSerializer)
    def create(self, request):
        serializer = PolicemanWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        policeman = serializer.create(serializer.validated_data)
        policeman_serialized = PolicemanReadSerializer(policeman)
        return Response(policeman_serialized.data)

    def retrieve(self, request, identification_number=None):
        queryset = Policeman.objects.all()
        policeman = get_object_or_404(queryset, identification_number=identification_number)
        policeman_serialized = PolicemanReadSerializer(policeman)
        return Response(policeman_serialized.data)

    @swagger_auto_schema(request_body=PolicemanWriteSerializer)
    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass