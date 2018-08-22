# Generated by Django 2.0.5 on 2018-06-02 09:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityDistrict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='区域')),
                ('desc', models.CharField(blank=True, max_length=200, null=True, verbose_name='描述')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '区域',
                'verbose_name_plural': '区域',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='公司名称')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='公司描述')),
                ('image', models.ImageField(blank=True, null=True, upload_to='company/%Y%m', verbose_name='封面')),
                ('address', models.CharField(max_length=150, verbose_name='公司地址')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('tag', models.CharField(default='全国知名', max_length=10, verbose_name='公司标签')),
                ('dist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CityDistrict', verbose_name='所在区域')),
            ],
            options={
                'verbose_name': '公司',
                'verbose_name_plural': '公司',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='员工名')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='employee/%Y/%m', verbose_name='头像')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.Company', verbose_name='所属公司')),
            ],
            options={
                'verbose_name': '员工',
                'verbose_name_plural': '员工',
            },
        ),
    ]