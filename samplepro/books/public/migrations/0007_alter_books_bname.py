# Generated by Django 4.2 on 2023-05-12 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0006_rename_name_books_bname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='bname',
            field=models.CharField(max_length=50),
        ),
    ]
