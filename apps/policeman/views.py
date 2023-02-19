from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from apps.policeman.models import Policeman
from apps.policeman.serializers import (
    PolicemanCreateSerializer,
    PolicemanReadSerializer,
    PolicemanUpdateSerializer,
    PolicemanUpdatePasswordSerializer
)


class PolicemanViewSet(ViewSet):
    def list(self, request):
        queryset = Policeman.objects.all()
        policemen_serialized = PolicemanReadSerializer(queryset, many=True)
        return Response(policemen_serialized.data)

    @swagger_auto_schema(request_body=PolicemanCreateSerializer)
    def create(self, request):
        serializer = PolicemanCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        policeman = serializer.create(serializer.validated_data)
        policeman_serialized = PolicemanReadSerializer(policeman)
        return Response(policeman_serialized.data)

    def retrieve(self, request, identification_number=None):
        queryset = Policeman.objects.all()
        policeman = get_object_or_404(queryset, identification_number=identification_number)
        policeman_serialized = PolicemanReadSerializer(policeman)
        return Response(policeman_serialized.data)

    @swagger_auto_schema(request_body=PolicemanUpdateSerializer)
    def update(self, request, identification_number=None):
        queryset = Policeman.objects.all()
        policeman = get_object_or_404(queryset, identification_number=identification_number)
        serializer = PolicemanUpdateSerializer(policeman, data=request.data)
        serializer.is_valid(raise_exception=True)
        policeman_updated = serializer.update(policeman, serializer.validated_data)
        policeman_updated_serialized = PolicemanReadSerializer(policeman_updated)
        return Response(policeman_updated_serialized.data)

    @action(detail=False)
    @swagger_auto_schema(request_body=PolicemanUpdatePasswordSerializer)
    def update_password(self, request, identification_number=None):
        queryset = Policeman.objects.all()
        policeman = get_object_or_404(queryset, identification_number=identification_number)
        serializer = PolicemanUpdatePasswordSerializer(policeman, data=request.data)
        serializer.is_valid(raise_exception=True)
        policeman_updated = serializer.update(policeman, serializer.validated_data)
        policeman_updated_serialized = PolicemanReadSerializer(policeman_updated)
        return Response(policeman_updated_serialized.data)

    def destroy(self, request, identification_number=None):
        queryset = Policeman.objects.all()
        policeman = get_object_or_404(queryset, identification_number=identification_number)
        policeman.delete()
        return Response({'response': 'the user was deleted successfully'})
