# Generated by Django 3.2.13 on 2022-06-30 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ricamo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=900),
        ),
    ]