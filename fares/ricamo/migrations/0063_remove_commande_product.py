# Generated by Django 3.2.13 on 2022-12-22 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ricamo', '0062_to_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='product',
        ),
    ]