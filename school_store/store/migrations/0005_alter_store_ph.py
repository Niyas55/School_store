# Generated by Django 4.2.3 on 2023-10-23 03:19

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_store_ph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='ph',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=10, region=None),
        ),
    ]
