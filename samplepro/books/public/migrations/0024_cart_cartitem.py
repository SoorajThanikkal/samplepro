# Generated by Django 4.2 on 2023-05-24 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0023_delete_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='public.register')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='public.books')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='public.cart')),
            ],
        ),
    ]
