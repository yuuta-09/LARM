from django.urls import path
from .views import SignUpView
from rest_framework_simplejwt.views import (
  TokenObtainPairView, TokenBlacklistView
)

urlpatterns = [
  path('signup/', SignUpView.as_view(), name='signup'),
  path('signin/', TokenObtainPairView.as_view(), name='signin'),
  path('signout/', TokenBlacklistView.as_view(), name='signout'),
]