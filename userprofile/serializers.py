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
            'is_staff'
        ]
        read_only_fields = [
            'username',
            'id',
            'balance',
            'is_premium_user',
            'is_staff'
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
        raise NotImplementedError

    @staticmethod
    def validate_password(value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
        return value


class UserChangePasswordSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(write_only=True,
                                         validators=[validate_password])

    class Meta:
        model = GLMUser
        fields = [
            'id',
            'username',
            'password',
            'new_password',
        ]
        read_only_fields = [
            'id',
            'username'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            old_password = validated_data.pop('password')
        else:
            raise serializers.ValidationError("Need Password.")
        if instance.check_password(old_password):
            if 'new_password' in validated_data:
                new_password = validated_data.pop('new_password')
                instance.set_password(new_password)
            return super().update(instance, validated_data)
        else:
            raise serializers.ValidationError("Wrong Password!")
