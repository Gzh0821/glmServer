from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
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


class AdminUpdateUserView(RetrieveUpdateDestroyAPIView):
    """
    管理员根据uuid管理普通用户,GET获取信息,PUT用于完整修改,PATCH用于部分字段修改,DELETE用于删除用户.
    """
    queryset = GLMUser.objects.filter(is_staff=False)
    serializer_class = AdminUserSettingSerializer
    permission_classes = [IsAdminUser]


class AdminUpdateUserByName(AdminUpdateUserView):
    """
    管理员根据用户名更新某个用户的信息.PUT用于完整修改用户信息,PATCH用于修改部分信息,如仅修改用户余额或密码.
    """
    lookup_field = 'username'


class AdminUpdateSelfView(RetrieveUpdateAPIView):
    """
    管理员更新自己的信息,PUT用于完整修改,PATCH用于部分字段修改.
    """
    serializer_class = AdminUserSettingSerializer
    permission_classes = [IsAdminUser]

    def get_object(self):
        return self.request.user
