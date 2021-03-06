# Generated by Django 3.2.6 on 2021-10-09 21:06

from django.db import migrations, models
import profanity.validators


class Migration(migrations.Migration):

    dependencies = [
        ('roommates', '0003_alter_user_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='about_me',
            field=models.CharField(blank=True, help_text='Short description about the user.', max_length=1024, null=True, validators=[profanity.validators.validate_is_profane], verbose_name='About Me'),
        ),
    ]
