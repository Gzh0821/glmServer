from django.urls import path
from archive import views

app_name = 'archive'

urlpatterns = [
    path('list', views.archive_list, name='list'),
]
