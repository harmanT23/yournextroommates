# Generated by Django 3.2.6 on 2021-08-04 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roommates', '0004_alter_user_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_picture',
        ),
    ]
