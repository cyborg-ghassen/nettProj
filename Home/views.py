from os import name
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import UpdateView
from django.views.generic.edit import DeleteView
from .forms import *
from .models import *

# Create your views here.
def homePage(request):
    if request.user.is_superuser:
        return render(request, 'home/superuser.html', {})
    else:
        return render(request, 'home/home.html', {})

def charts(request):
    return render(request, 'pages/chartjs.html', {})

def Users(request):
    return render(request, 'pages/basic-table.html', {})

def addProduct(request):
    context = {}
    if request.method == "POST":
        form = addProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            description = form.cleaned_data.get("description")
            img = form.cleaned_data.get("image")
            category = form.cleaned_data.get("category")
            price = form.cleaned_data.get("price")
            quantity = form.cleaned_data.get("quantity")
            obj = Product.objects.create(
                                 name = name,
                                 description=description,
                                 image = img,
                                 category = category,
                                 price = price,
                                 quantity = quantity
                                 )
            obj.save()
            print(obj)
    else:
        form = addProductForm()
    context['form'] = form

    return render(request, 'pages/add-product.html', context)

def viewProduct(request):
    product = Product.objects.all()
    return render(request, 'pages/view-product.html', {
        'product':product
    })

def editProduct(request):
    product = Product.objects.all()
    return render(request, 'pages/edit-product.html', {
        'product':product
    })

class EditProductView(UpdateView):
    model = Product
    form_class = editProductForm
    template_name = "pages/product-edit.html"

    def get_object(self, *args, **kwargs):
        product = get_object_or_404(Product, pk=self.kwargs['pk'])

        # We can also get user object using self.request.user  but that doesnt work
        # for other models.

        return product

    def get_success_url(self, *args, **kwargs):
        return reverse("edit_prod")

class MyDeleteView(DeleteView):
    model = Product
    success_url = "/product-delete/"


def deleteProduct(request):
    product = Product.objects.all()
    return render(request, 'pages/delete-product.html', {
        'product':product
    })

def addCategory(request):
    return render(request, 'pages/add-category.html', {})

def viewCategory(request):
    return render(request, 'pages/view-category.html', {})

def editCategory(request):
    return render(request, 'pages/edit-category.html', {})

def deleteCategory(request):
    return render(request, 'pages/delete-category.html', {})