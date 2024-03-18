from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile
from products.models import Product

# Create your models here.

class Wishlist(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
    related_name='wishlist')
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('wishlist', kwargs={'pk': self.pk})

class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name