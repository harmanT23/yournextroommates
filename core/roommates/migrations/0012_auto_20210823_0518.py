# Generated by Django 3.2.6 on 2021-08-23 05:18

from django.db import migrations, models
import roommates.models


class Migration(migrations.Migration):

    dependencies = [
        ('roommates', '0011_alter_listing_rent_per_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='extra_expenses_per_month',
            field=models.DecimalField(decimal_places=2, help_text='Extra expenses per month between $0.00 to $9,999.99.', max_digits=6, validators=[roommates.models.validate_prices], verbose_name='Extra Expenses Per Month'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='rent_per_month',
            field=models.DecimalField(decimal_places=2, help_text='Rent per month between $0.00 to $9,999.99.', max_digits=6, validators=[roommates.models.validate_prices], verbose_name='Rent Per Month'),
        ),
    ]
