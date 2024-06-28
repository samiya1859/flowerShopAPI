from django.db import models
from userApp.models import UserModel
from products.models import Product

from django.db import models
from userApp.models import UserModel
from products.models import Product

class Cart(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.product.name} (x{self.quantity})"

    def item_total(self):
        return self.product.price * self.quantity



class Purchase(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_purchased = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.product.name} (x{self.quantity}) on {self.date_purchased}"

class Wishlist(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.product.name} (added on {self.added_on})"
