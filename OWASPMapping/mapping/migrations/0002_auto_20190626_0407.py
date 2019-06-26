# Generated by Django 2.1.5 on 2019-06-26 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_oas_errordetails',
            name='id',
        ),
        migrations.RemoveField(
            model_name='tbl_oas_errorlevels',
            name='id',
        ),
        migrations.RemoveField(
            model_name='tbl_oas_errortypes',
            name='id',
        ),
        migrations.AlterField(
            model_name='tbl_oas_errordetails',
            name='detail_id',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tbl_oas_errorlevels',
            name='level_id',
            field=models.CharField(max_length=2, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tbl_oas_errortypes',
            name='error_id',
            field=models.CharField(max_length=3, primary_key=True, serialize=False),
        ),
    ]