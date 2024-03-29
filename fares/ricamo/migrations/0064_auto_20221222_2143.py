# Generated by Django 3.2.13 on 2022-12-22 21:43

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ricamo', '0063_remove_commande_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='color',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='quantite',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='size',
        ),
        migrations.AddField(
            model_name='to_order',
            name='color',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=None),
        ),
        migrations.AddField(
            model_name='to_order',
            name='quantite',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='to_order',
            name='size',
            field=models.CharField(default='Standart', max_length=3),
        ),
    ]
