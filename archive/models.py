from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class ChatArchive(models.Model):
    # 用户
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='ArchiveToUser'
    )
    # 聊天内容
    body = models.JSONField()
    # 时间戳
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.body)
