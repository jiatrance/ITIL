from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    gender_choices={('male','男'),('female','女')}
    name=models.CharField('姓名',max_length=50,default='')
    birthday=models.DateField('生日',null=True,blank=True)
    gender=models.CharField('性别',max_length=10,choices=gender_choices,default='female')
    address=models.CharField('地址',max_length=100,default='',null=True,blank=True)
    mobile=models.CharField('手机号',max_length=11,null=True,blank=True)
    image=models.ImageField(upload_to='img/%Y%M',default='media/img/default.jpg',verbose_name='头像',max_length=100,null=True,blank=True)
    email = models.EmailField('邮箱',max_length=50,default='',null=True,blank=True)
    add_time=models.DateTimeField(default=datetime.now)

    POSITION = (
        ("junior", u"初级工程师"),
        ("normal", u"工程师"),
        ("special", u"高级工程师"),
    )

    category = models.CharField(max_length=20, choices=POSITION, verbose_name=u"职位类别", default="normal")

    class Meta:
        verbose_name='用户信息'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name


