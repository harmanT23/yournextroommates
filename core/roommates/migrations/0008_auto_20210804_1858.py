# Generated by Django 3.2.6 on 2021-08-04 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roommates', '0007_alter_listing_poster'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='room_type',
        ),
        migrations.DeleteModel(
            name='RoomTypes',
        ),
    ]
