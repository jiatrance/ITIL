# Generated by Django 2.0.5 on 2018-06-17 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0020_auto_20180615_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='指派给'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='order.Category', verbose_name='故障类型'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='company',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='organization.Company', verbose_name='公司'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='customer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='organization.Employee', verbose_name='员工'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='priority',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='order.Priority', verbose_name='优先级'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='resolution_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.Resolution', verbose_name='解决类型'),
        ),
    ]
