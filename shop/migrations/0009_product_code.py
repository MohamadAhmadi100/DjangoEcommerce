# Generated by Django 3.2 on 2021-04-28 22:49

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20210428_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='code',
            field=models.IntegerField(default=shop.models.random_int),
        ),
    ]
