from rest_framework import serializers

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
            'password',
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
            'date_joined',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)
