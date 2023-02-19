from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.vehicle.views import VehicleViewSet

urlpatterns = [
    path('', VehicleViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='vehicle-list'),
    path('<str:plate>/', VehicleViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='vehicle-detail')
]