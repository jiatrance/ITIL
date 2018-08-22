# Generated by Django 2.0.5 on 2018-06-05 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_auto_20180605_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='statue',
            field=models.CharField(blank=True, choices=[('new', '新建'), ('active', '激活'), ('reassigned', '重派'), ('pending', '挂起'), ('update', '更新'), ('resolved', '已解决')], default='new', max_length=10, null=True, verbose_name='状态'),
        ),
    ]
