# Generated by Django 3.2.6 on 2021-08-24 05:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('roommates', '0014_auto_20210824_0453'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Gallery', 'verbose_name_plural': 'Gallery'},
        ),
        migrations.AddField(
            model_name='gallery',
            name='uuid',
            field=models.CharField(default=uuid.uuid4, help_text='Name of gallery is unique UUID. Generated on instance creation.', max_length=36, unique=True, verbose_name='UUID'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='created_at',
            field=models.DateTimeField(auto_now=True, help_text='Indicates when gallery instance was created.', verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='listing',
            field=models.ForeignKey(blank=True, help_text='Gallery belongs to associated listing.', null=True, on_delete=django.db.models.deletion.CASCADE, to='roommates.listing', verbose_name='Listing'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Indicates when gallery instance was last updated.', verbose_name='Updated At'),
        ),
    ]