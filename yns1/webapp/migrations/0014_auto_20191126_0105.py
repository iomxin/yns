# Generated by Django 2.2.6 on 2019-11-25 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_auto_20191126_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='detail',
            field=models.TextField(max_length=10000),
        ),
    ]
