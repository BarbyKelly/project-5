# Generated by Django 3.2.25 on 2025-02-25 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
    ]
