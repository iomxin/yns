# Generated by Django 2.2.6 on 2019-11-19 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_auto_20191119_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to='static/image/'),
        ),
        migrations.AlterField(
            model_name='course',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='static/image/'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to='static/image/'),
        ),
    ]
