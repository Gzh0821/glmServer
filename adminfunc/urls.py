from django.urls import path

from adminfunc import views

app_name = 'adminfunc'

urlpatterns = [
    path('listuser/', views.AdminUserListView.as_view(), name='listuser'),
    path('edituser/uuid/<uuid:pk>/', views.AdminUpdateUserView.as_view(), name='edit-uuid'),
    path('edituser/username/<str:username>/', views.AdminUpdateUserByName.as_view(), name='edit-uuid'),
    path('editself/', views.AdminUpdateSelfView.as_view(), name='edit-self'),
]
