# Generated by Django 2.0.5 on 2018-06-14 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0018_auto_20180614_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='指派给'),
        ),
    ]
