# Generated by Django 2.2.6 on 2019-11-19 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='course',
        ),
    ]
