# Generated by Django 4.0.3 on 2022-03-04 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_remove_product_product_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_stock',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]