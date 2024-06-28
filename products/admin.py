from django.contrib import admin
from .models import Fields, Category, Product, Review


class FieldsAdmin(admin.ModelAdmin):
    list_display = ('field', 'slug')
    prepopulated_fields = {'slug': ('field',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'slug')
    prepopulated_fields = {'slug': ('category',)}

admin.site.register(Fields,FieldsAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product)
admin.site.register(Review)