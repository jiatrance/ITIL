# Generated by Django 2.0.5 on 2018-06-17 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_remove_company_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': '部门', 'verbose_name_plural': '部门'},
        ),
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(max_length=150, verbose_name='部门地址'),
        ),
        migrations.AlterField(
            model_name='company',
            name='desc',
            field=models.TextField(blank=True, null=True, verbose_name='部门描述'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=50, verbose_name='部门名称'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.Company', verbose_name='所属部门'),
        ),
    ]
