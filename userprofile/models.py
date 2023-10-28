from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """
    用户扩展模型
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    balance = models.IntegerField(default=0)
    is_premium_user = models.BooleanField(default=False)

    def __str__(self):
        return 'user {}'.format(self.user.username)


# 创建信号
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# 修改信号
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# 删除信号
# @receiver(post_delete, sender=User)
# def delete_user_profile(sender, instance, **kwargs):
#     instance.userprofile.delete()
