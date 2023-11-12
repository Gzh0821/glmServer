import random
import string

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from adminfunc.models import InvitationCode
from adminfunc.serializers import AdminUserSettingSerializer, InvitationCodeSerializer
from userprofile.models import GLMUser
from userprofile.serializers import UserBaseInfoSerializer


class AdminUserListView(generics.ListAPIView):
    """
    管理员获取用户列表.
    """
    queryset = GLMUser.objects.all()
    serializer_class = UserBaseInfoSerializer
    permission_classes = [IsAdminUser]


class AdminUpdateUserView(generics.RetrieveUpdateDestroyAPIView):
    """
    管理员根据uuid管理普通用户,GET获取信息,PUT用于完整修改,PATCH用于部分字段修改,DELETE用于删除用户.
    """
    queryset = GLMUser.objects.filter(is_staff=False)
    serializer_class = AdminUserSettingSerializer
    permission_classes = [IsAdminUser]


class AdminUpdateUserByName(AdminUpdateUserView):
    """
    管理员根据用户名更新某个用户的信息.PUT用于完整修改用户信息,PATCH用于修改部分信息,如仅修改用户余额.
    """
    lookup_field = 'username'


class AdminUpdateSelfView(generics.RetrieveUpdateAPIView):
    """
    管理员更新自己的信息,PUT用于完整修改,PATCH用于部分字段修改.
    """
    serializer_class = AdminUserSettingSerializer
    permission_classes = [IsAdminUser]

    def get_object(self):
        return self.request.user


class InvitationCodeViewSet(generics.ListAPIView):
    """
    管理员获取自己生成的邀请码列表.
    """
    serializer_class = InvitationCodeSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        queryset = InvitationCode.objects.filter(created_by=self.request.user)
        return queryset


class InvitationDeleteViewSet(generics.DestroyAPIView):
    """
    管理员根据邀请码id删除邀请码.
    """
    serializer_class = InvitationCodeSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        queryset = InvitationCode.objects.filter(created_by=self.request.user.id)
        return queryset


class GenerateInvitationCode(APIView):
    permission_classes = [IsAdminUser]

    @staticmethod
    def _generate_invitation_code(length):
        if length > 20 or length < 1:
            length = 8
        characters = string.ascii_letters + string.digits  # 使用字母和数字
        code = ''.join(random.choice(characters) for _ in range(length))
        return code

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['length'],
            properties={
                'length': openapi.Schema(type=openapi.TYPE_INTEGER),
            }
        ),
        responses={201: openapi.Response('', InvitationCodeSerializer), },
        operation_description="根据输入的长度生成邀请码."
    )
    def post(self, request):
        # 生成邀请码的逻辑
        length = int(request.data.get('length', 8))
        code = self._generate_invitation_code(length)  # 你需要实现生成邀请码的函数
        obj = InvitationCode.objects.create(code=code, created_by=request.user)
        return Response(InvitationCodeSerializer(obj).data, status=status.HTTP_201_CREATED)
