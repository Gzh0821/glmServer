from django.urls import path
from userprofile import views

app_name = 'userprofile'

urlpatterns = [
    path('info', views.user_base_info, name='info'),
]