from django.db import models

CATEGORIES = (
    ('1', ''),
)

# Create your models here.
class Product(models.Model):
    name = models.CharField(verbose_name="Product Name:", max_length=80)
    description = models.TextField(verbose_name="Product Description:", max_length=300)
    image = models.ImageField(verbose_name="Product Image:", upload_to='static/')
    category = models.CharField(choices=CATEGORIES, verbose_name="Product Category:", max_length=100)
    price = models.CharField(verbose_name="Product Price:", max_length=80)
    quantity = models.IntegerField(verbose_name="Product Quantity:")