from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from userprofile.serializers import UserBaseInfoSerializer


class UserProfileAPIView(RetrieveAPIView):
    """
    获取当前用户的基本信息.
    """
    serializer_class = UserBaseInfoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # 返回当前登录用户的Profile实例
        return self.request.user.profile
