from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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
        read_only_fields = [
            'username',
            'id',
            'balance',
            'is_premium_user'
        ]


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
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
        user = User.objects.create_user(**validated_data)
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
