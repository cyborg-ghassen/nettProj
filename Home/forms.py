from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = "__all__"

class addProductForm(forms.ModelForm):
    name = forms.CharField(label="Product Name:", max_length=80)
    description = forms.TextInput()
    category = forms.CharField(label="Product Category:", max_length=100)
    price = forms.CharField(label="Product Price:", max_length=80)
    quantity = forms.IntegerField(label="Product Quantity:")

    class Meta:
        model = Product
        fields = ["name", "description", "image", "category", "price", "quantity"]