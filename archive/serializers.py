from rest_framework import serializers

from archive.models import ChatArchive


class ArchiveListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatArchive
        fields = [
            'id',
            'user',
            'body',
            'timestamp'
        ]
        read_only_fields = [
            'id',
            'user',
            'body',
            'timestamp'
        ]


class ArchiveDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatArchive
        fields = '__all__'
        read_only_fields = [
            'id',
            'user',
            'timestamp'
        ]
