# Generated by Django 3.2.13 on 2022-07-12 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ricamo', '0026_rename_order_date_commande_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='date',
        ),
    ]
