# Generated by Django 4.2 on 2023-05-12 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0002_category_books'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='bname',
        ),
    ]
