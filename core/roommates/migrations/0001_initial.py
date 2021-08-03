# Generated by Django 3.2.6 on 2021-08-03 19:26

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import roommates.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('profile_picture', models.ImageField(null=True, upload_to='')),
                ('date_of_birth', models.DateField()),
                ('about_me', models.CharField(max_length=500)),
                ('university', models.CharField(max_length=80)),
                ('university_major', models.CharField(max_length=50)),
                ('profession', models.CharField(max_length=80)),
                ('home_city', models.CharField(max_length=32)),
                ('home_province', models.CharField(max_length=25)),
                ('current_city', models.CharField(max_length=32)),
                ('current_province', models.CharField(max_length=25)),
                ('is_lister', models.BooleanField()),
                ('is_seeker', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=1024)),
                ('address2', models.CharField(max_length=10)),
                ('postal_code', models.CharField(max_length=5)),
                ('city', models.CharField(max_length=32)),
                ('province', models.CharField(max_length=25)),
                ('room_desc', models.CharField(max_length=1024)),
                ('is_furnished', models.BooleanField()),
                ('number_current_residents', models.PositiveIntegerField()),
                ('rent_per_month', models.DecimalField(decimal_places=2, max_digits=7)),
                ('additional_expenses_per_month', models.DecimalField(decimal_places=2, max_digits=6)),
                ('earliest_move_in_date', models.DateField()),
                ('latest_move_in_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('poster', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoomTypes',
            fields=[
                ('id', models.PositiveSmallIntegerField(choices=[(1, 'bedroom'), (2, 'shared_bedroom'), (3, 'den'), (4, 'living_room'), (5, 'shared_living_room'), (6, 'sunroom'), (7, 'closet')], primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=roommates.models.upload_user_gallery_image)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ListingImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=roommates.models.upload_listing_gallery_image)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roommates.listing')),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='room_type',
            field=models.ManyToManyField(to='roommates.RoomTypes'),
        ),
    ]