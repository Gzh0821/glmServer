from rest_framework.decorators import api_view
from rest_framework.response import Response

from userprofile.models import Profile
from userprofile.serializers import UserBaseInfoSerializer
from django.contrib.auth.decorators import login_required


@api_view(['GET'])
@login_required
def user_base_info(request):
    """
    获取当前用户的基本信息.
    :param request:
    :return:
    """
    current_user = request.user
    records = Profile.objects.get(user=current_user)
    serializer = UserBaseInfoSerializer(records)
    return Response(serializer.data)
