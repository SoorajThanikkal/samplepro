# Generated by Django 4.2 on 2023-05-12 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0003_rename_name_category_bname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='Bookfor',
        ),
        migrations.RemoveField(
            model_name='books',
            name='Category',
        ),
        migrations.AddField(
            model_name='books',
            name='name',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
