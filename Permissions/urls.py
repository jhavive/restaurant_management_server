
from rest_framework.routers import DefaultRouter
from .views import PermissionsViewSet

router = DefaultRouter()
router.register(r'Permissions/permissions', PermissionsViewSet, basename='permissions')

urlpatterns = router.urls