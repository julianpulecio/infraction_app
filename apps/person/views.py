from django.shortcuts import render

# Create your views here.
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ViewSet

from apps.person.serializers import PersonSerializer


class PersonViewSet(ViewSet):
    def list(self, request):
        pass

    @swagger_auto_schema(request_body=PersonSerializer)
    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    @swagger_auto_schema(request_body=PersonSerializer)
    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass