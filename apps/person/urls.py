from django.urls import path
from apps.person.views import PersonViewSet

urlpatterns = [
    path('', PersonViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='person-list'),
    path('<str:email>/', PersonViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='person-detail'),
    path('generar_informe/<str:email>/', PersonViewSet.as_view({
        'get': 'get_all_infractions'
    }), name='person-infractions'),
]