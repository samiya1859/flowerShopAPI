from rest_framework import serializers
from .models import Cart, Purchase, Wishlist

class CartSerializer(serializers.ModelSerializer):
    item_total = serializers.ReadOnlyField()

    class Meta:
        model = Cart
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'
