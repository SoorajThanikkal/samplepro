# Generated by Django 4.2 on 2023-05-18 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0016_alter_books_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='public.books')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='public.register')),
            ],
        ),
    ]