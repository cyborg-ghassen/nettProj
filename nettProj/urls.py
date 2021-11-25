"""nettProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from Home.views import *
from register.views import *
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name="Home"),
    path("register/", register, name="register"),
    path("charts/", charts, name="charts"),
    path("users/", Users, name="users"),
    path("users-list", readUsers, name="users-read"),
    path("product-add/", addProduct, name="add_prod"),
    path("product-view/", viewProduct, name="view_prod"),
    path("product-edit/", editProduct, name="edit_prod"),
    url(r'^product/(?P<pk>\d+)/edit/$', EditProductView.as_view(), name="edit-product"),
    path("product-delete/", deleteProduct, name="delete_prod"),
    path("delete_url/<pk>/", MyDeleteView.as_view()),
    path("category-add/", addCategory, name="add_cat"),
    path("category-view/", viewCategory, name="view_cat"),
    path("users-edit/", editUser, name="edit_users"),
    url(r'^user/(?P<pk>\d+)/edit/$', EditUserView.as_view(), name="edit-user"),
    path("user-delete/", deleteUser, name="delete_user"),
    path("delete_user/<pk>/", MyDeleteUserView.as_view()),
    url(r'^category/(?P<pk>\d+)/edit/$', EditCategoryView.as_view(), name="edit-category"),
    path("category-edit/", editCategory, name="edit_cat"),
    path("category-delete/", deleteCategory, name="delete_cat"),
    path("delete_cat/<pk>/", MyDeleteCategoryView.as_view()),
    path('', include("django.contrib.auth.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
