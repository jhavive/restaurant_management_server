"""ekom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

#custom views
from .views.tables import TablesViewSet
from .views.menu import MenuViewSet
from .views.qr import get_qr, get_qr_pdf
from .views.orders import OrdersViewSet
# from .views.orders import OrderViewSet


router = DefaultRouter()
router.register(r'tables/tables', TablesViewSet, basename='tables')
router.register(r'tables/order', OrdersViewSet, basename='order')
router.register(r'menu/menu', MenuViewSet, basename='menu')


urlpatterns = router.urls + [path('qr', get_qr), path('qr-pdf', get_qr_pdf)]


