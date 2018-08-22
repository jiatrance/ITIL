# Generated by Django 2.0.6 on 2018-06-09 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_workorder_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.Employee', verbose_name='员工'),
        ),
    ]
