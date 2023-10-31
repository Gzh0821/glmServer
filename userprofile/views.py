from rest_framework.generics import RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from userprofile.serializers import UserBaseInfoSerializer, UserRegisterSerializer, UserChangePasswordSerializer


class UserProfileAPIView(RetrieveAPIView):
    """
    获取当前用户的基本信息.
    """
    serializer_class = UserBaseInfoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # 返回当前登录用户的Profile实例
        return self.request.user


class UserRegistrationView(CreateAPIView):
    """
    注册一个新用户.
    """
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]


class UserChangePasswordView(UpdateAPIView):
    """
    修改用户密码.
    """
    serializer_class = UserChangePasswordSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['put']

    def get_object(self):
        return self.request.user
