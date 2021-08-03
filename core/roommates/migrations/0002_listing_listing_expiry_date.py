# Generated by Django 3.2.6 on 2021-08-03 19:45

from django.db import migrations, models
import roommates.models


class Migration(migrations.Migration):

    dependencies = [
        ('roommates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='listing_expiry_date',
            field=models.DateField(default=roommates.models.default_expiry_date),
        ),
    ]