from django.db import models

from userprofile.models import GLMUser


# Create your models here.
class InvitationCode(models.Model):
    code = models.CharField(max_length=20, unique=True)
    is_used = models.BooleanField(default=False)
    created_by = models.ForeignKey(GLMUser, on_delete=models.CASCADE)  # 与创建者关联
    created_at = models.DateTimeField(auto_now_add=True)
