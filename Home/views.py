from os import name
from django.shortcuts import redirect, render
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
    category = Category.objects.all()
    if request.method == "POST":
        form = addProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = addProductForm()

    return render(request, 'pages/add-product.html', {'form':form, 'category':category})

def viewProduct(request):
    return render(request, 'pages/view-product.html', {})

def editProduct(request):
    return render(request, 'pages/edit-product.html', {})

def deleteProduct(request):
    return render(request, 'pages/delete-product.html', {})

def addCategory(request):
    return render(request, 'pages/add-category.html', {})

def viewCategory(request):
    return render(request, 'pages/view-category.html', {})

def editCategory(request):
    return render(request, 'pages/edit-category.html', {})

def deleteCategory(request):
    return render(request, 'pages/delete-category.html', {})