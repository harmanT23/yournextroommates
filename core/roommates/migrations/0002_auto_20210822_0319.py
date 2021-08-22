# Generated by Django 3.2.6 on 2021-08-22 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roommates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='home_city',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AddField(
            model_name='user',
            name='home_province',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='user',
            name='current_city',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='current_province',
            field=models.CharField(max_length=25),
        ),
    ]
