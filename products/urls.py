from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FieldsViewSet, CategoryViewSet, ProductViewSet, ReviewViewSet

router = DefaultRouter()
router.register('fields', FieldsViewSet)
router.register('categories', CategoryViewSet)
router.register('reviews', ReviewViewSet)
router.register('list', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
