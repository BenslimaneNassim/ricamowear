# Generated by Django 3.2.13 on 2022-07-14 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ricamo', '0035_auto_20220714_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='selled',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=7),
            preserve_default=False,
        ),
    ]