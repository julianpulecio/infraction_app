from rest_framework.routers import DefaultRouter
from apps.policeman.views import PolicemanViewSet


router = DefaultRouter()
router.register('', PolicemanViewSet, basename='policeman')
urlpatterns = router.urls