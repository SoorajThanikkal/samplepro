# Generated by Django 4.2 on 2023-05-24 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0020_remove_register_address_remove_register_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='public.books')),
            ],
        ),
    ]
