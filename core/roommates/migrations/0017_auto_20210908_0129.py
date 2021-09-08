# Generated by Django 3.2.6 on 2021-09-08 01:29

from django.db import migrations, models
import django.db.models.deletion
import roommates.image_handlers
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('roommates', '0016_auto_20210824_0545'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Image file within the associated gallery', upload_to=roommates.image_handlers.upload_gallery_image, verbose_name='Image')),
                ('image_name', models.CharField(blank=True, help_text='Name of image', max_length=36, null=True, unique=True, verbose_name='Path')),
                ('created_at', models.DateTimeField(auto_now=True, help_text='Indicates when image instance was created.', verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Indicates when image instance was last updated.', verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Gallery Image',
                'verbose_name_plural': 'Gallery Images',
            },
        ),
        migrations.RemoveField(
            model_name='userimagegallery',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Gallery', 'verbose_name_plural': 'Galleries'},
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='is_listing_gallery',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='is_user_gallery',
        ),
        migrations.AddField(
            model_name='gallery',
            name='is_listing_or_user_gallery',
            field=models.BooleanField(default=False, help_text='Gallery belongs to Listing if true, else for User', verbose_name='Is Listing Gallery'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gallery',
            name='uuid',
            field=models.CharField(default=uuid.uuid4, help_text='Name of gallery is its UUID. Generated on instance creation.', max_length=36, unique=True, verbose_name='UUID'),
        ),
        migrations.DeleteModel(
            name='ListingImageGallery',
        ),
        migrations.DeleteModel(
            name='UserImageGallery',
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='gallery',
            field=models.ForeignKey(help_text='Image belongs to associated Gallery.', on_delete=django.db.models.deletion.CASCADE, to='roommates.gallery', verbose_name='Gallery'),
        ),
    ]
