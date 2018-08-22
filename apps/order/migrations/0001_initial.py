# Generated by Django 2.0.5 on 2018-06-02 09:13

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_type', models.CharField(max_length=30, verbose_name='故障类型')),
            ],
            options={
                'verbose_name': '故障类型',
                'verbose_name_plural': '故障类型',
            },
        ),
        migrations.CreateModel(
            name='Resolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resolution_code', models.CharField(max_length=30, verbose_name='解决类型')),
            ],
            options={
                'verbose_name': '解决类型',
                'verbose_name_plural': '解决类型',
            },
        ),
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=30, verbose_name='工单号')),
                ('company', models.CharField(max_length=50, verbose_name='公司')),
                ('phone', models.IntegerField(max_length=11, verbose_name='电话')),
                ('priority', models.CharField(choices=[('std', '普通'), ('high', '高级'), ('urgent', '紧急')], max_length=10, verbose_name='优先级')),
                ('attachment', models.FileField(upload_to='order/resource/%Y/%m', verbose_name='附件')),
                ('statue', models.CharField(choices=[('new', '新建'), ('active', '激活'), ('reassigned', '重派'), ('pending', '挂起'), ('update', '更新'), ('resolved', '已解决')], default='new', max_length=10, verbose_name='状态')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('description', models.TextField(verbose_name='描述')),
                ('followup_notes', models.TextField(verbose_name='更新类容')),
                ('resolution_notes', models.TextField(verbose_name='解决方案')),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='指派给')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Categoty', verbose_name='故障类型')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.Company', verbose_name='员工')),
                ('resolution_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Resolution', verbose_name='解决类型')),
            ],
            options={
                'verbose_name': '工单',
                'verbose_name_plural': '工单',
            },
        ),
    ]