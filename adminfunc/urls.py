from django.urls import path

from adminfunc import views

app_name = 'adminfunc'

urlpatterns = [
    path('listuser/', views.AdminUserListView.as_view(), name='listuser'),
    path('edituser/uuid/<uuid:pk>/', views.AdminUpdateUserView.as_view(), name='edit-uuid'),
    path('edituser/username/<str:username>/', views.AdminUpdateUserByName.as_view(), name='edit-uuid'),
    path('editself/', views.AdminUpdateSelfView.as_view(), name='edit-self'),
    path('invite/list/', views.InvitationCodeViewSet.as_view(), name='invitation'),
    path('invite/gen/', views.GenerateInvitationCode.as_view(), name='generate-invitation'),
    path('invite/delete/<int:pk>/', views.InvitationDeleteViewSet.as_view(), name='delete-invitation')
]
