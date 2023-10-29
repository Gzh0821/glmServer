from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from userprofile import views

app_name = 'userprofile'

urlpatterns = [
    path('info', views.UserProfileAPIView.as_view(), name='info'),
    path('token/get', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('register', views.UserRegistrationView.as_view(), name='register')
]
