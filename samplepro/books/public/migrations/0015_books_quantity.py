# Generated by Django 4.2 on 2023-05-18 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0014_alter_books_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='quantity',
            field=models.PositiveIntegerField(default='0'),
        ),
    ]