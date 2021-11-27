from django.contrib import admin
from .models import *
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        ('User data', {
            "fields": (
                'phone',
                'is_product_manager',
                'is_stock_manager',
                'is_agent',
                'is_simple_user',
            ),
        }),
    )
    

admin.site.register(User, CustomUserAdmin)
admin.site.register(UserRating)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
