# Generated by Django 3.2.13 on 2022-07-12 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ricamo', '0027_remove_commande_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
