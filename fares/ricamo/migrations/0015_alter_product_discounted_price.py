# Generated by Django 3.2.13 on 2022-07-02 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ricamo', '0014_product_discounted_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discounted_price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=7),
        ),
    ]
