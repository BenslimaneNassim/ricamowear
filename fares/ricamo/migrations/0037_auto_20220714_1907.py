# Generated by Django 3.2.13 on 2022-07-14 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ricamo', '0036_commande_selled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discounted_price',
            field=models.IntegerField(blank=True, default=None, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(max_length=7),
        ),
    ]
