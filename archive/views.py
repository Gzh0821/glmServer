from django.contrib.auth.decorators import login_required
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from archive.example import generate_text
from archive.models import ChatArchive
from archive.serializers import ArchiveListSerializer, ArchiveDetailSerializer
from userprofile.models import GLMUser


class ArchiveListView(ListAPIView):
    """
    获取当前用户的所有生成记录列表.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = ArchiveListSerializer

    def get_queryset(self):
        return ChatArchive.objects.filter(user=self.request.user)


class ArchiveDetailView(RetrieveAPIView):
    """
    获取指定id的详细生成记录.
    """
    queryset = ChatArchive.objects.all()
    serializer_class = ArchiveDetailSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.is_superuser or instance.user == request.user:
            return super().retrieve(request, *args, **kwargs)
        else:
            return Response(
                {"error": "Permission denied."},
                status=status.HTTP_403_FORBIDDEN
            )


@swagger_auto_schema(
    method='POST',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['body'],
        properties={
            'body': openapi.Schema(type=openapi.TYPE_STRING),
        }
    ),
    responses={
        201: openapi.Response('', ArchiveDetailSerializer),
        400: openapi.Response('', ArchiveDetailSerializer),
        402: openapi.Response('Account Not enough balance.'),
    }
)
@api_view(['POST'])
@login_required
def create_new_chat(request):
    """
    创建新的生成对话.
    """
    user_profile = GLMUser.objects.get(id=request.user.id)
    if user_profile.balance <= 0:
        return Response(
            {"error": "Payment Required."},
            status=status.HTTP_402_PAYMENT_REQUIRED
        )
    body = request.data.get('body')
    data = {"body": body}
    serializer = ArchiveDetailSerializer(data=data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        prompt = generate_text(body)
        serializer.save(prompt=prompt)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CreateNewChatView(CreateAPIView):
#     queryset = ChatArchive.objects.all()
#     serializer_class = ArchiveDetailSerializer
#
#     def perform_create(self, serializer):
#         # 设置 user 字段为当前请求的用户
#         serializer.save(user=self.request.user)
#
#     def create(self, request, *args, **kwargs):
#         # 从请求数据中提取 'body' 字段
#         body_data = request.data.get('body')
#
#         # 创建一个字典包含要传递给序列化器的数据
#         data_to_serialize = {'body': body_data}
#
#         serializer = self.get_serializer(data=data_to_serialize)
#         if serializer.is_valid():
#             self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
