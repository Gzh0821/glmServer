from django.urls import path

from archive import views

app_name = 'archive'

urlpatterns = [
    path('list', views.ArchiveListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.ArchiveDetailView.as_view(), name='detail')
]
