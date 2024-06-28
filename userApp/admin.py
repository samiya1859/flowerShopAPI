from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserModel

class CustomUserAdmin(UserAdmin):
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone', 'address', 'shop_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_customer', 'is_seller', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Fields to be used when creating a new user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'phone', 'address', 'shop_name', 'is_customer', 'is_seller')}
        ),
    )
    
    # Fields to be displayed in the list view.
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_customer', 'is_seller', 'is_staff')
    
    # Fields to filter the user list by.
    list_filter = ('is_staff', 'is_superuser', 'is_customer', 'is_seller', 'is_active', 'groups')
    
    # Fields that can be used to search in the admin interface.
    search_fields = ('username', 'first_name', 'last_name', 'email')
    
    ordering = ('username',)

# Register the custom admin class with the UserModel
admin.site.register(UserModel, CustomUserAdmin)
