# Generated by Django 4.2 on 2023-05-28 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0031_buyer_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='quantity',
        ),
    ]