from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Infraction API",
        default_version='v1',
        description="This is a project to manage the infractions and their related entities",
        terms_of_service="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        contact=openapi.Contact(email="julianpuleciogomez@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)