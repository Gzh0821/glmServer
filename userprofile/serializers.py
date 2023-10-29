from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from userprofile.models import GLMUser


class UserBaseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GLMUser
        fields = [
            'username',
            'id',
            'balance',
            'is_premium_user',
        ]
        read_only_fields = [
            'username',
            'id',
            'balance',
            'is_premium_user',
        ]


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = GLMUser
        fields = [
            'id',
            'username',
            'password',
            'date_joined'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }
        read_only_fields = [
            'id',
            'date_joined'
        ]

    def create(self, validated_data):
        user = GLMUser.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)

    @staticmethod
    def validate_password(value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
        return value
