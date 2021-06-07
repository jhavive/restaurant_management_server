from django.urls import path,include, re_path
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import UsersViewSet
from django.http import JsonResponse

def handle_options(request):
    if request.method == 'OPTIONS':
        return JsonResponse(data={}, status=200)

router = DefaultRouter()
router.register(r'custom_user/user', UsersViewSet, basename='users')

# urlpatterns = [re_path('users/', handle_options, name='handle_options')] + router.urls
urlpatterns = router.urls