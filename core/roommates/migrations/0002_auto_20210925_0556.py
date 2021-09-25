# Generated by Django 3.2.6 on 2021-09-25 05:56

from django.db import migrations, models
import profanity.validators


class Migration(migrations.Migration):

    dependencies = [
        ('roommates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(help_text='First name of user.', max_length=50, validators=[profanity.validators.validate_is_profane], verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(help_text='Last name of user.', max_length=50, validators=[profanity.validators.validate_is_profane], verbose_name='Last Name'),
        ),
    ]