# Generated by Django 4.2 on 2023-05-28 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0032_remove_buyer_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
