# Generated by Django 3.2.25 on 2024-09-10 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_image_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
