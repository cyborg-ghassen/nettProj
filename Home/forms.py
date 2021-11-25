from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = "__all__"

class addUserForm(forms.ModelForm):
    username = forms.CharField(label="User name:", max_length=80)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    phone = forms.CharField(label="Phone number:", max_length=80)
    is_product_manager = forms.CheckboxInput()
    is_stock_manager = forms.CheckboxInput()
    is_agent = forms.CheckboxInput()
    is_simple_user = forms.CheckboxInput()

    class Meta:
        model = User
        fields = ("username", "email", "password", "phone", "is_product_manager", "is_stock_manager", "is_agent", "is_simple_user")

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

class addCategoryForm(forms.ModelForm):
    name = forms.CharField(label="Category Name:", max_length=80)

    class Meta:
        model = Category
        fields = ("name", )

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

class editCategoryForm(forms.ModelForm):
    name = forms.CharField(label="Product Name:", max_length=80)

    class Meta:
        model = Category
        fields = ("name", )


    def save(self, category=None):
        category = super(editCategoryForm, self).save(commit=False)
        if category:
            category = category
        category.save()
        return category

class editUserForm(forms.ModelForm):
    username = forms.CharField(label="User name:", max_length=80)
    email = forms.EmailField()
    phone = forms.CharField(label="Phone number:", max_length=80)
    is_product_manager = forms.CheckboxInput()
    is_stock_manager = forms.CheckboxInput()
    is_agent = forms.CheckboxInput()
    is_simple_user = forms.CheckboxInput()

    class Meta:
        model = User
        fields = ("username", "email",  "phone", "is_product_manager", "is_stock_manager", "is_agent", "is_simple_user")


    def save(self, users=None):
        users = super(editUserForm, self).save(commit=False)
        if users:
            users = users
        users.save()
        return users