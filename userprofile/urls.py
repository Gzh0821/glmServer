from django.urls import path
from userprofile import views

app_name = 'userprofile'

urlpatterns = [
    path('info', views.UserProfileAPIView.as_view(), name='info'),
]