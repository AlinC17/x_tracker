from rest_framework import routers
from django.urls import path, include
from apps.tracker.views import DeviceViewSet, DeviceModelViewSet, suggestions

app_name = 'tracker'
router = routers.DefaultRouter()
router.register(r'devices', DeviceViewSet, basename='devices')
router.register('device/models', DeviceModelViewSet, basename='device-models')

urlpatterns = [
    path('address/suggestions', suggestions, name='suggestions'),
    path('', include(router.urls)),
]