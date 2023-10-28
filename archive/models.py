from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class ChatArchive(models.Model):
    # 用户
    user = models.ForeignKey(
        User,
        null=False,
        on_delete=models.CASCADE,
        related_name='ArchiveToUser'
    )
    # 输入信息
    body = models.TextField(max_length=100)
    # glm生成的提示词
    prompt = models.TextField(blank=True)
    # 结果
    res = models.TextField(blank=True)
    # 时间戳
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.body)
