# Generated by Django 2.0.6 on 2018-06-09 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20180609_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('female', '女'), ('male', '男')], default='female', max_length=10, verbose_name='性别'),
        ),
    ]