# Generated by Django 2.2.6 on 2019-11-25 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_remove_choice_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='quiz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.Quiz'),
        ),
    ]
