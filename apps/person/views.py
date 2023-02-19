from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from apps.person.models import Person
from apps.person.serializers import PersonSerializer


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

    @swagger_auto_schema(request_body=PersonSerializer)
    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass