from django.db import models
from datetime import datetime


class CityDistrict(models.Model):
    name=models.CharField('区域',max_length=20)
    desc=models.CharField('描述',max_length=200,null=True,blank=True)
    add_time=models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name='区域'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name


class Company(models.Model):
    name=models.CharField('部门名称',max_length=50)
    desc=models.TextField('部门描述',null=True,blank=True)
    image = models.ImageField('封面', upload_to='company/%Y%m', max_length=100,null=True,blank=True)
    address=models.CharField('部门地址',max_length=150)
    dist=models.ForeignKey(CityDistrict,verbose_name='所在区域',on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name='部门'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name


class Employee(models.Model):
    employee_id=models.CharField('工号',max_length=20,default='')
    company = models.ForeignKey(Company, verbose_name='所属部门', on_delete=models.CASCADE)
    name = models.CharField('员工名', max_length=50)
    phone=models.CharField('电话',max_length=11,default='')
    image = models.ImageField(
        default='',
        upload_to="employee/%Y/%m",
        verbose_name="头像",
        max_length=100,
        null=True,
        blank=True
    )
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name='员工'
        verbose_name_plural=verbose_name

    def __str__(self):
        return '[{0}]的员工：{1}'.format(self.company,self.name)

