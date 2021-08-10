# Generated by Django 3.2.6 on 2021-08-09 01:43

from django.db import migrations
import roommates.managers


class Migration(migrations.Migration):

    dependencies = [
        ('roommates', '0017_auto_20210809_0139'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', roommates.managers.CustomUserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]