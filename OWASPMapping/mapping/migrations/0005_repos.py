# Generated by Django 2.1.5 on 2019-06-26 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0004_auto_20190626_0526'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name_plural': 'repositories',
            },
        ),
    ]