# Generated by Django 3.1.7 on 2021-02-23 05:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UpdateCountDown',
            new_name='Notice',
        ),
    ]
