# Generated by Django 4.2 on 2023-05-12 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0005_alter_books_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='name',
            new_name='bname',
        ),
    ]
