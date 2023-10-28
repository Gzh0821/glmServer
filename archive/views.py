from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from archive.models import ChatArchive
from archive.serializers import ArchiveListSerializer, ArchiveDetailSerializer


class ArchiveListView(ListAPIView):
    """
    获取当前用户的所有对话记录.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = ArchiveListSerializer

    def get_queryset(self):
        return ChatArchive.objects.filter(user=self.request.user)


class ArchiveDetailView(RetrieveAPIView):
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
