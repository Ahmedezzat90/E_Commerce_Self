# Generated by Django 4.2.4 on 2023-09-22 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Carts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='quantity',
        ),
    ]
