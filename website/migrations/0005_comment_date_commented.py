# Generated by Django 3.1.7 on 2021-02-25 06:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20210225_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_commented',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
