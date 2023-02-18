from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.policeman.views import PolicemanViewSet

# router = DefaultRouter()
# router.register('', PolicemanViewSet, basename='policeman')
urlpatterns = [
    path('/', PolicemanViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='policeman-list'),
    path('/<int:identification_number>/', PolicemanViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='policeman-detail'),
]
