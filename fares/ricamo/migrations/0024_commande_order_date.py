# Generated by Django 3.2.13 on 2022-07-12 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ricamo', '0023_auto_20220712_0216'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='order_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
