# Generated by Django 3.2.13 on 2022-12-20 16:34

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ricamo', '0052_auto_20221220_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='color',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=None),
        ),
    ]
