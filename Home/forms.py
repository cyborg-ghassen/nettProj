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
    image = forms.ImageField()
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label="Product Category:",
                widget = forms.Select(attrs={
                    'class':'form-control'
                })
    )
    price = forms.CharField(label="Product Price:", max_length=80)
    quantity = forms.IntegerField(label="Product Quantity:")

    class Meta:
        model = Product
        fields = ("name", "description", "image", "category", "price", "quantity")

class editProductForm(forms.ModelForm):
    name = forms.CharField(label="Product Name:", max_length=80)
    description = forms.TextInput()
    image = forms.ImageField()
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label="Product Category:",
                widget = forms.Select(attrs={
                    'class':'form-control'
                })
    )
    price = forms.CharField(label="Product Price:", max_length=80)
    quantity = forms.IntegerField(label="Product Quantity:")

    class Meta:
        model = Product
        fields = ("name", "description", "image", "category", "price", "quantity")


    def save(self, product=None):
        product = super(editProductForm, self).save(commit=False)
        if product:
            product = product
        product.save()
        return product