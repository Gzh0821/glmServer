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
