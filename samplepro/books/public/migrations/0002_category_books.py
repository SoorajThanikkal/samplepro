# Generated by Django 4.2 on 2023-05-12 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField()),
                ('price', models.FloatField()),
                ('author', models.CharField(max_length=10)),
                ('Bookfor', models.CharField(choices=[('Buy', 'Buy'), ('Return', 'Return'), ('Sell', 'Sell')], default='Buy', max_length=20)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='public.category')),
            ],
        ),
    ]