# Generated by Django 3.2.13 on 2022-07-02 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ricamo', '0017_alter_product_discounted_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discounted_price',
        ),
    ]
