# Generated by Django 3.2.13 on 2022-12-19 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ricamo', '0047_email_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Hoodie', 'Hoodie'), ('Sweater', 'Sweater'), ('Ensemble', 'Ensemble'), ('Bag', 'Bag'), ('T-Shirt', 'T-Shirt')], max_length=30),
        ),
        migrations.AlterField(
            model_name='design',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
