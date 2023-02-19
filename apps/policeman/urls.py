from django.urls import path
from apps.policeman.views import PolicemanViewSet

urlpatterns = [
    path('', PolicemanViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='policeman-list'),
    path('<int:identification_number>/', PolicemanViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='policeman-detail'),
    path('password_update/<int:identification_number>/', PolicemanViewSet.as_view({
        'put': 'update_password',
    }), name='policeman-password-update'),
]
