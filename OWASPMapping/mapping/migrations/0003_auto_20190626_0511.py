# Generated by Django 2.1.5 on 2019-06-26 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0002_auto_20190626_0407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_oas_errordetaillevels',
            name='user_id',
        ),
        migrations.AddField(
            model_name='tbl_oas_errordetails',
            name='level_1',
            field=models.CharField(default='1', max_length=1),
        ),
        migrations.AddField(
            model_name='tbl_oas_errordetails',
            name='level_2',
            field=models.CharField(default='1', max_length=1),
        ),
        migrations.AddField(
            model_name='tbl_oas_errordetails',
            name='level_3',
            field=models.CharField(default='1', max_length=1),
        ),
        migrations.DeleteModel(
            name='tbl_OAS_ERRORDETAILLEVELS',
        ),
    ]
