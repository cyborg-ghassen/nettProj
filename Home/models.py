from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

CATEGORIES = (
    ('1', ''),
)



class User(AbstractUser):
    phone = models.CharField(verbose_name="Phone number:", max_length=80)
    is_product_manager = models.BooleanField(verbose_name="Is Product Manager", default=False)
    is_stock_manager = models.BooleanField(verbose_name="Is Stock Manager", default=False)
    is_agent = models.BooleanField(verbose_name="Is Agent", default=False)
    is_simple_user = models.BooleanField(verbose_name="Is Simple User", default=True)
    email = models.EmailField("email address", unique=True)

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(verbose_name="Category Name:", max_length=80)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

# Create your models here.
class Product(models.Model):
    name = models.CharField(verbose_name="Product Name:", max_length=80)
    description = models.TextField(verbose_name="Product Description:", max_length=300)
    image = models.ImageField(verbose_name="Product Image:", upload_to='static/')
    category = models.ForeignKey(Category, verbose_name="Product Category:", max_length=100, on_delete=models.CASCADE)
    price = models.CharField(verbose_name="Product Price:", max_length=80)
    quantity = models.IntegerField(verbose_name="Product Quantity:")

    def __str__(self):
        return self.name

