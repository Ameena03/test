# Generated by Django 3.1.6 on 2021-07-03 04:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0004_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='ooooo',
        ),
    ]
