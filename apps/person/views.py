from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from apps.person.models import Person
from apps.person.serializers import PersonSerializer, PersonUpdateSerializer


class PersonViewSet(ViewSet):
    def list(self, request):
        queryset = Person.objects.all()
        person_serialized = PersonSerializer(queryset, many=True)
        return Response(person_serialized.data)

    @swagger_auto_schema(request_body=PersonSerializer)
    def create(self, request):
        serializer = PersonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        person = serializer.create(serializer.validated_data)
        person_serialized = PersonSerializer(person)
        return Response(person_serialized.data)

    def retrieve(self, request, email=None):
        queryset = Person.objects.all()
        person = get_object_or_404(queryset, email=email)
        person_serialized = PersonSerializer(person)
        return Response(person_serialized.data)

    @swagger_auto_schema(request_body=PersonUpdateSerializer)
    def update(self, request, email=None):
        queryset = Person.objects.all()
        person = get_object_or_404(queryset, email=email)
        serializer = PersonUpdateSerializer(person, data=request.data)
        serializer.is_valid(raise_exception=True)
        person_updated = serializer.update(person, serializer.validated_data)
        person_updated_serialized = PersonSerializer(person_updated)
        return Response(person_updated_serialized.data)

    def destroy(self, request, email=None):
        queryset = Person.objects.all()
        person = get_object_or_404(queryset, email=email)
        person.delete()
        return Response({'response': 'the person was deleted successfully'})