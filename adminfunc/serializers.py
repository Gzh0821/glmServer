from rest_framework import serializers

from adminfunc.models import InvitationCode
from userprofile.models import GLMUser


class AdminUserSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GLMUser
        fields = [
            'id',
            'username',
            'is_superuser',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'is_active',
            'date_joined',
            'balance',
            'is_premium_user'
        ]
        read_only_fields = [
            'id',
            'username',
            'is_superuser',
            'is_staff',
            'date_joined',
        ]


class InvitationCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvitationCode
        fields = '__all__'
        read_only_fields = [
            'created_at'
        ]
