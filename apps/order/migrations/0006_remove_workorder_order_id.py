# Generated by Django 2.0.5 on 2018-06-02 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20180602_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workorder',
            name='order_id',
        ),
    ]
