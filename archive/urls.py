from django.urls import path

from archive import views

app_name = 'archive'

urlpatterns = [
    path('list', views.ArchiveListView.as_view(), name='list'),
    path('detail/<uuid:pk>', views.ArchiveDetailView.as_view(), name='detail'),
    path('create', views.create_new_chat, name='create'),
    path('delete/<uuid:pk>', views.ArchiveDeleteView.as_view(), name='destroy')
    # path('new/', views.CreateNewChatView.as_view(), name='new'),
]
