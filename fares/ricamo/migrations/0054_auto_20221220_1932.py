# Generated by Django 3.2.13 on 2022-12-20 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ricamo', '0053_commande_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='l_size',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='color',
            name='m_size',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='color',
            name='s_size',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='color',
            name='standart_size',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='color',
            name='xl_size',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='color',
            name='xxl_size',
            field=models.BooleanField(default=True),
        ),
    ]
