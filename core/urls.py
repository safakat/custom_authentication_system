from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from core.backends import LoginAPIView

urlpatterns = [
    path('login',LoginAPIView.as_view(), name='login'),
    path('refresh_token',TokenRefreshView.as_view(), name='refresh_token')
]