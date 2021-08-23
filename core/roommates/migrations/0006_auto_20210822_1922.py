# Generated by Django 3.2.6 on 2021-08-22 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import roommates.models


class Migration(migrations.Migration):

    dependencies = [
        ('roommates', '0005_auto_20210822_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='poster',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listingimagegallery',
            name='image',
            field=models.ImageField(default='images/listings/default.jpg', upload_to=roommates.models.upload_listing_gallery_image, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='userimagegallery',
            name='image',
            field=models.ImageField(default='images/users/gallery/default.jpg', upload_to=roommates.models.upload_user_gallery_image, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='userprofileimage',
            name='profile_picture',
            field=models.ImageField(blank=True, default='images/users/profile/default.jpeg', upload_to=roommates.models.upload_user_profile_image, verbose_name='Image'),
        ),
    ]
