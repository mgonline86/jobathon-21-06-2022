from .views import PersonViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', PersonViewSet, basename='persons')
urlpatterns = router.urls