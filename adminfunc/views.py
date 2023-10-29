from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAdminUser

from adminfunc.serializers import AdminUserSettingSerializer
from userprofile.models import GLMUser
from userprofile.serializers import UserBaseInfoSerializer


class AdminUserListView(ListAPIView):
    """
    管理员获取用户列表.
    """
    queryset = GLMUser.objects.all()
    serializer_class = UserBaseInfoSerializer
    permission_classes = [IsAdminUser]


class AdminUpdateUserView(UpdateAPIView):
    """
    管理员根据uuid更新某个用户的信息.PUT用于完整修改用户信息,PATCH用于修改部分信息,如仅修改用户余额或密码.
    """
    queryset = GLMUser.objects.all()
    serializer_class = AdminUserSettingSerializer
    permission_classes = [IsAdminUser]

    def perform_update(self, serializer):
        serializer.save()


class AdminUpdateUserByName(AdminUpdateUserView):
    """
    管理员根据用户名更新某个用户的信息.PUT用于完整修改用户信息,PATCH用于修改部分信息,如仅修改用户余额或密码.
    """
    lookup_field = 'username'
