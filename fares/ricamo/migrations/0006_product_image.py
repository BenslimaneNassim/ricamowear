# Generated by Django 3.2.13 on 2022-07-01 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ricamo', '0005_commande'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product-images-display/'),
        ),
    ]