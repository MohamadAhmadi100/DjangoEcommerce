# Generated by Django 3.2 on 2021-04-28 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20210428_1902'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Price',
            new_name='price',
        ),
    ]