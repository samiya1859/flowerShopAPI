from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Fields, Category, Product, Review
from .serializers import FieldsSerializer, CategorySerializer, ProductSerializer, ReviewSerializer

class FieldsViewSet(viewsets.ModelViewSet):
    queryset = Fields.objects.all()
    serializer_class = FieldsSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['field', 'category']
    search_fields = ['name', 'category__category', 'field__field']


class ReviewFilterbyProduct(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        product = request.query_params.get('product')
        print(product)
        if product:
            return queryset.filter(product=product)
        return queryset
    
class ReviewFilterbyUser(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        user = request.query_params.get('user')
        print(user)
        if user:
            return queryset.filter(user=user)
        return queryset

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [ReviewFilterbyProduct,ReviewFilterbyUser]
    filterset_fields = ['user', 'product']
