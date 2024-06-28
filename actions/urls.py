from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet, PurchaseViewSet, WishlistViewSet

router = DefaultRouter()
router.register('carts', CartViewSet)
router.register('purchases', PurchaseViewSet)
router.register('wishlists', WishlistViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
