from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

# custom urls
# from inventory import urls

urlpatterns = [
    path('', include(views.login)),
    path('/get-routes', include(views.get_routes)),
]


