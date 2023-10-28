from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from archive.models import ChatArchive
from archive.serializers import ArchiveListSerializer
from django.contrib.auth.decorators import login_required


@api_view(['GET'])
@login_required
def archive_list(request):
    """
    获取当前用户的所有对话记录.
    :param request:
    :return:
    """
    current_user = request.user
    records = ChatArchive.objects.filter(user=current_user)
    serializer = ArchiveListSerializer(records, many=True)
    return Response(serializer.data)
