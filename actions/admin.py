from django.contrib import admin
from .models import Cart, Purchase, Wishlist

admin.site.register(Cart)
admin.site.register(Purchase)
admin.site.register(Wishlist)