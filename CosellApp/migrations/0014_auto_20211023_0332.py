# Generated by Django 3.1.4 on 2021-10-23 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CosellApp', '0013_auto_20211021_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='transection_id',
            field=models.CharField(default='NONE', max_length=30),
        ),
    ]
