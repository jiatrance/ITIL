# Generated by Django 2.0.6 on 2018-06-09 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_auto_20180609_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resolutions',
            name='resolution_code',
        ),
        migrations.AddField(
            model_name='workorder',
            name='followup_notes',
            field=models.TextField(blank=True, null=True, verbose_name='更新类容'),
        ),
        migrations.AddField(
            model_name='workorder',
            name='resolution_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.Resolution', verbose_name='解决类型'),
        ),
        migrations.AddField(
            model_name='workorder',
            name='resolution_notes',
            field=models.TextField(blank=True, null=True, verbose_name='解决方案'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='comment',
            field=models.TextField(blank=True, default='', null=True, verbose_name='备注'),
        ),
        migrations.DeleteModel(
            name='Resolutions',
        ),
    ]
