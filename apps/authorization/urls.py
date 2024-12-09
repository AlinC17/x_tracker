from django.urls import path
from django.conf import settings
from apps.authorization.views import login, logout
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView


app_name = "authorization"
if settings.USE_JWT:
    urlpatterns = [
        path('login/', TokenObtainPairView.as_view(), name='login'),
        path('refresh/', TokenRefreshView.as_view(), name='refresh'),
        path('logout/', TokenBlacklistView.as_view(), name='logout'),
    ]
else:
    urlpatterns = [
        path('login/', login, name='login'),
        path('logout/', logout, name='logout'),
    ]
