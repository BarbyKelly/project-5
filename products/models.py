# this file is based on Code Institute's Boutique Ado walk-through, like all the files and folders in this project
from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    author = models.TextField(max_length=50)
    description = models.TextField(max_length=300)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.name
