# Generated by Django 2.0.6 on 2018-06-09 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_auto_20180606_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='workorder',
            name='comment',
            field=models.TextField(default='', verbose_name='备注'),
        ),
    ]