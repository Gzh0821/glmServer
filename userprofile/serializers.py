from rest_framework import serializers

from userprofile.models import Profile


class UserBaseInfoSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    id = serializers.IntegerField(source='user.id')

    class Meta:
        model = Profile
        fields = [
            'username',
            'id',
            'balance',
            'is_premium_user'
        ]
