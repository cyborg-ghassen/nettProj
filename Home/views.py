from os import name
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Sum
from django.http import JsonResponse
from django.views.generic import UpdateView, DetailView
from django.views.generic.edit import DeleteView
from .forms import *
from .models import *
from hitcount.views import HitCountDetailView

# Create your views here.
def homePage(request):
    products = Product.objects.all()
    users = User.objects.all()
    users_count = users.count()
    user_rating = 0
    bounce_rate = 0
    for i in users:
        user_rating += get_object_or_404(UserRating, user=i).rating
        bounce_rate = (user_rating / users_count) * 100 / users_count
    if request.user.is_superuser:
        return render(request, 'home/superuser.html', {
            'users_count':users_count,
            'bounce_rate':bounce_rate
            })
    else:
        return render(request, 'home/home.html', {
            'latest_products': products[:3]
        })

def productDetailView(request, slug):
    context = {}
    context['product'] = Product.objects.get(slug=slug)
    return render(request, 'home/product_detail.html', context)

def addOrder(request, id):
    product = Product.objects.get(id=id)
    obj = Order.objects.create(product=product, user=request.user)
    obj.save()

    return redirect("detail", slug=product.slug)

def charts(request):
    labels = []
    data = []
    quantities = []

    queryset = Product.objects.order_by('-price')[:5]
    for product in queryset:
        labels.append(product.name)
        data.append(product.price)
        quantities.append(product.quantity)

    return render(request, 'pages/chartjs.html', {
        'labels': labels,
        'data': data,
        'quantities':quantities
    })

def Users(request):
    context = {}
    if request.method == "POST":
        form = addUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            phone = form.cleaned_data.get("phone")
            is_product_manager = form.cleaned_data.get("is_product_manager")
            is_stock_manager = form.cleaned_data.get("is_stock_manager")
            is_agent = form.cleaned_data.get("is_agent")
            is_simple_user = form.cleaned_data.get("is_simple_user")
            obj = User.objects.create(
                                 username = username,
                                 email=email,
                                 password = password,
                                 phone = phone,
                                 is_product_manager = is_product_manager,
                                 is_stock_manager = is_stock_manager,
                                 is_agent = is_agent,
                                 is_simple_user = is_simple_user
                                 )
            obj.save()
            print(obj)
    else:
        form = addUserForm()
    context['form'] = form
    return render(request, 'pages/basic-table.html', context)

def readUsers(request):
    users = User.objects.all()
    return render(request, 'pages/users-read.html', {'users':users})

def editUser(request):
    users = User.objects.all()
    return render(request, 'pages/edit-users.html', {
        'users':users
    })

class EditUserView(UpdateView):
    model = User
    form_class = editUserForm
    template_name = "pages/user-edit.html"

    def get_object(self, *args, **kwargs):
        user = get_object_or_404(User, pk=self.kwargs['pk'])

        # We can also get user object using self.request.user  but that doesnt work
        # for other models.

        return user

    def get_success_url(self, *args, **kwargs):
        return reverse("edit_users")

class MyDeleteUserView(DeleteView):
    model = User
    success_url = "/user-delete/"


def deleteUser(request):
    user = User.objects.all()
    return render(request, 'pages/delete-user.html', {
        'user':user
    })

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
    context = {}
    if request.method == "POST":
        form = addCategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            obj = Category.objects.create(name = name)
            obj.save()
            print(obj)
    else:
        form = addCategoryForm()
    context['form'] = form

    return render(request, 'pages/add-category.html', context)

def viewCategory(request):
    category = Category.objects.all()
    return render(request, 'pages/view-category.html', {'category':category})

class EditCategoryView(UpdateView):
    model = Category
    form_class = editCategoryForm
    template_name = "pages/category-edit.html"

    def get_object(self, *args, **kwargs):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])

        # We can also get user object using self.request.user  but that doesnt work
        # for other models.

        return category

    def get_success_url(self, *args, **kwargs):
        return reverse("edit_cat")


def editCategory(request):
    category = Category.objects.all()
    return render(request, 'pages/edit-category.html', {'category':category})

class MyDeleteCategoryView(DeleteView):
    model = Category
    success_url = "/category-delete/"


def deleteCategory(request):
    category = Category.objects.all()
    return render(request, 'pages/delete-category.html', {
        'category':category
    })

class ProductDetailView(HitCountDetailView):
    model = Product
    template = 'superuser.html'
    # set to True to count the hit
    count_hit = True

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return context