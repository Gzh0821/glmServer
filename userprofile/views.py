from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from userprofile.serializers import UserBaseInfoSerializer, UserRegisterSerializer


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
