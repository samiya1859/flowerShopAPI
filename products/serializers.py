from rest_framework import serializers
from .models import Fields, Category, Product, Review
from userApp.models import UserModel

class FieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fields
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    field = FieldsSerializer()
    category = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    product = ProductSerializer()

    class Meta:
        model = Review
        fields = '__all__'
