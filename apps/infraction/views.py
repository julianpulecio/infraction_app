from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from apps.infraction.serializers import InfractionSerializer, InfractionReadSerializer


class InfractionViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=InfractionSerializer)
    def create(self, request):
        serializer = InfractionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        infraction = serializer.custom_create(serializer.validated_data, request.user)
        infraction_serialized = InfractionReadSerializer(infraction)
        return Response(infraction_serialized.data)
