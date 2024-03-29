# Generated by Django 3.2.13 on 2022-12-20 16:16

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ricamo', '0050_alter_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=colorfield.fields.ColorField(blank=True, default=None, image_field=None, max_length=18, null=True, samples=None),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='category-images-display/'),
        ),
    ]
