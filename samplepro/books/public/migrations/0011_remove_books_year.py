# Generated by Django 4.2 on 2023-05-16 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0010_alter_register_usergrand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='year',
        ),
    ]
