# Generated by Django 2.0.5 on 2018-06-02 09:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20180602_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_type', models.CharField(max_length=30, verbose_name='故障类型')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '故障类型',
                'verbose_name_plural': '故障类型',
            },
        ),
        migrations.AddField(
            model_name='resolution',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Category', verbose_name='故障类型'),
        ),
        migrations.DeleteModel(
            name='Categoty',
        ),
    ]
