# Generated by Django 3.2.13 on 2022-07-01 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ricamo', '0009_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='l_size',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='m_size',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='s_size',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='xl_size',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='xxl_size',
            field=models.BooleanField(default=False),
        ),
    ]
