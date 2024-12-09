from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularRedocView, SpectacularAPIView


api_patterns = [
       path('tracker/', include('apps.tracker.urls', 'tracker')),
       path('auth/', include('apps.authorization.urls', 'authorization')),
]

urlpatterns = [
       path('admin/', admin.site.urls),
       path('api/', include(api_patterns)),
       path('docs/schema/', SpectacularAPIView.as_view(), name='schema'),
       path('docs/swagger/', SpectacularSwaggerView.as_view(), name='swagger'),
       path('docs/redoc/', SpectacularRedocView.as_view(), name='redoc'),
]
