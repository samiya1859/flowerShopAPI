from django.db import models
from userApp.models import UserModel

# Create your models here.

STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

class Fields(models.Model):
    field = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True)

    def __str__(self) -> str:
        return self.field

class Category(models.Model):
    category = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True)

    def __str__(self) -> str:
        return self.category

class Product(models.Model):
    name = models.CharField(max_length=50)
    field = models.ForeignKey(Fields, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    sold = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Review(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField(choices=STAR_CHOICES)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self) -> str:
        return f'Review of {self.product.name} by {self.user.username}'
