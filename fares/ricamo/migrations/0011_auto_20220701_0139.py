# Generated by Django 3.2.13 on 2022-07-01 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ricamo', '0010_auto_20220701_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='l_size',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='m_size',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='s_size',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='xl_size',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='xxl_size',
            field=models.IntegerField(default=0),
        ),
    ]