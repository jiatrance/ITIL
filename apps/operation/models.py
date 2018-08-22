from django.db import models
from users.models import UserProfile
from datetime import datetime
from order.models import WorkOrder


class UserComments(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    work_order = models.ForeignKey(WorkOrder, verbose_name='工单', on_delete=models.CASCADE)
    comments = models.CharField('评论', max_length=200)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '跟进情况'
        verbose_name_plural = verbose_name
