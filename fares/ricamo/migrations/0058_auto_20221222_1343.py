# Generated by Django 3.2.13 on 2022-12-22 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ricamo', '0057_alter_shipping_price_wilaya'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shipping_price',
            old_name='price',
            new_name='price_bureau',
        ),
        migrations.AddField(
            model_name='shipping_price',
            name='price_domicile',
            field=models.IntegerField(default=600),
        ),
    ]