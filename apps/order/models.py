from django.db import models
from organization.models import Company,Employee
from users.models import UserProfile
from datetime import datetime


class Category(models.Model):
    case_type=models.CharField('故障类型',max_length=30)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name='故障类型'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.case_type


class Resolution(models.Model):
    resolution_code = models.CharField('解决类型', max_length=30)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '解决类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.resolution_code


class Priority(models.Model):
    priority = models.CharField('优先级', max_length=30)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '优先级'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.priority


class Statue(models.Model):
    status = models.CharField('状态', max_length=30)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '状态'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.status


class WorkOrder(models.Model):
    employee_id=models.CharField('员工号',max_length=20,default='')
    company=models.ForeignKey(Company,verbose_name='公司',on_delete=models.SET_DEFAULT,default='')
    customer=models.ForeignKey(Employee,verbose_name='员工',on_delete=models.SET_DEFAULT,default='')
    phone=models.CharField('电话',max_length=15,default='')
    category=models.ForeignKey(Category,verbose_name='故障类型',on_delete=models.SET_DEFAULT,default='')
    add_time = models.DateTimeField('添加时间', default=datetime.now)
    close_time = models.DateTimeField('关闭时间', default=datetime.now)
    priority=models.ForeignKey(Priority,verbose_name='优先级',on_delete=models.SET_DEFAULT,default='')
    attachment=models.FileField('附件',upload_to='order/resource/%Y/%m',max_length=100,null=True,blank=True)
    statue=models.ForeignKey(Statue,verbose_name='状态',on_delete=models.CASCADE,default='')
    assigned_to=models.ForeignKey(UserProfile,verbose_name='指派给',on_delete=models.SET_NULL,null=True,blank=True)
    title=models.CharField('标题',max_length=100)
    description=models.TextField('描述')
    comment=models.TextField('备注',default='',null=True,blank=True)
    resolution_code=models.ForeignKey(Resolution,verbose_name='解决类型',on_delete=models.SET_NULL,null=True,blank=True)
    followup_notes=models.TextField('更新类容',null=True,blank=True)
    resolution_notes=models.TextField('解决方案',null=True,blank=True)
    done=models.BooleanField(default=False)

    class Meta:
        verbose_name='工单'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.title
