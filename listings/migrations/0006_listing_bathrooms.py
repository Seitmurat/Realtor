# Generated by Django 4.0.2 on 2022-05-11 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_remove_listing_bathrooms'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='bathrooms',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=2),
            preserve_default=False,
        ),
    ]
