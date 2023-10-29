from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from userprofile.serializers import UserBaseInfoSerializer, UserUpdateSerializer


class UserProfileAPIView(RetrieveAPIView):
    """
    获取当前用户的基本信息.
    """
    serializer_class = UserBaseInfoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # 返回当前登录用户的Profile实例
        return self.request.user.profile


class UserRegistrationView(CreateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [AllowAny]
