# Generated by Django 3.2.13 on 2022-07-01 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ricamo', '0011_auto_20220701_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Hoodie', 'Hoodie'), ('Sweater', 'Sweater'), ('Ensemble', 'Ensemble'), ('Bag', 'Bag'), ('T-Shirt', 'T-Shirt')], max_length=8),
        ),
        migrations.AlterField(
            model_name='product',
            name='types',
            field=models.CharField(choices=[('Cloths', 'Cloth'), ('Accessories', 'Accessorie')], max_length=11),
        ),
    ]
