# Generated by Django 4.2 on 2023-05-16 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0012_books_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.CharField(default='', max_length=25),
        ),
    ]
