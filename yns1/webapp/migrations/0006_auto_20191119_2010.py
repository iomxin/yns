# Generated by Django 2.2.6 on 2019-11-19 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_course_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='img',
            field=models.FileField(null=True, upload_to='static'),
        ),
        migrations.AlterField(
            model_name='course',
            name='img',
            field=models.FileField(null=True, upload_to='static'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='img',
            field=models.FileField(null=True, upload_to='static'),
        ),
    ]
