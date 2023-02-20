from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.decorators import action, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from app.permissions import PermissionsPerMethodMixin
from apps.person.models import Person
from apps.person.serializers import PersonSerializer, PersonUpdateSerializer
from apps.infraction.serializers import InfractionVehiclesSerializer


class PersonViewSet(PermissionsPerMethodMixin,ViewSet):

    @permission_classes((permissions.IsAuthenticated,))
    def list(self, request):
        queryset = Person.objects.all()
        person_serialized = PersonSerializer(queryset, many=True)
        return Response(person_serialized.data)

    @swagger_auto_schema(request_body=PersonSerializer)
    @permission_classes((permissions.IsAuthenticated,))
    def create(self, request):
        serializer = PersonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        person = serializer.create(serializer.validated_data)
        person_serialized = PersonSerializer(person)
        return Response(person_serialized.data)

    @permission_classes((permissions.IsAuthenticated,))
    def retrieve(self, request, email=None):
        queryset = Person.objects.all()
        person = get_object_or_404(queryset, email=email)
        person_serialized = PersonSerializer(person)
        return Response(person_serialized.data)

    @swagger_auto_schema(request_body=PersonUpdateSerializer)
    @permission_classes((permissions.IsAuthenticated,))
    def update(self, request, email=None):
        queryset = Person.objects.all()
        person = get_object_or_404(queryset, email=email)
        serializer = PersonUpdateSerializer(person, data=request.data)
        serializer.is_valid(raise_exception=True)
        person_updated = serializer.update(person, serializer.validated_data)
        person_updated_serialized = PersonSerializer(person_updated)
        return Response(person_updated_serialized.data)

    @action(detail=False)
    @permission_classes((permissions.AllowAny,))
    def get_all_infractions(self, request, email=None):
        queryset = Person.objects.all()
        person = get_object_or_404(queryset, email=email)
        person_vehicles_query_set = person.vehicles.all()
        person_infractions= InfractionVehiclesSerializer(person_vehicles_query_set, many=True)
        return Response(person_infractions.data)

    @permission_classes((permissions.IsAuthenticated,))
    def destroy(self, request, email=None):
        queryset = Person.objects.all()
        person = get_object_or_404(queryset, email=email)
        person.delete()
        return Response({'response': 'the person was deleted successfully'})