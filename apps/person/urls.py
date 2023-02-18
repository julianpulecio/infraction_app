from rest_framework.routers import DefaultRouter
from apps.person.views import PersonViewSet


router = DefaultRouter()
router.register('', PersonViewSet, basename='person')
urlpatterns = router.urls