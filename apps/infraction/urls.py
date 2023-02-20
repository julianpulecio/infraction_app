from django.urls import path
from apps.infraction.views import InfractionViewSet

urlpatterns = [
    path('', InfractionViewSet.as_view({
        'post': 'create'
    }), name='infraction-create'),
]