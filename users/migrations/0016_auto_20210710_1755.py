# Generated by Django 3.1.6 on 2021-07-10 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20210710_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='p_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
