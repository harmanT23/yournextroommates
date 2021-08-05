# Generated by Django 3.2.6 on 2021-08-04 17:47

from django.db import migrations, models
import roommates.models


class Migration(migrations.Migration):

    dependencies = [
        ('roommates', '0003_auto_20210803_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, default='default.jpeg', upload_to=roommates.models.upload_user_profile_image),
        ),
    ]
