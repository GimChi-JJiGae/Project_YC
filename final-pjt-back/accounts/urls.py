from django.urls import path, include
from accounts import views

from rest_framework import routers
from accounts.views import UserViewSet
router = routers.DefaultRouter()
router.register('user', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]