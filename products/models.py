from django.db import models


# Code from Code Institute Boutique Ado Walksthrough
# Slightly modified model by adding description
class Category(models.Model):
    """
    Represents a category for products.
    Attributes:
        name (CharField): The name of the category.
        friendly_name (CharField): A more user-friendly name for the category,
        optional.
        description (TextField): A description of the category.
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        """ Returns the name of the category."""
        return self.name

    def get_friendly_name(self):
        """ Returns the friendly name of the category. """
        return self.friendly_name


# Minor adjusment of model by adding artist and is_print
class Product(models.Model):
    """
    Represents a product, associated with a category.
    Attributes:
        category (ForeignKey): The category this product belongs to, optional.
        sku (CharField): Stock Keeping Unit, a unique identifier for each
        product, optional.
        name (CharField): The name of the product.
        description (TextField): A description of the product.
        is_print (BooleanField): Indicates if the product is a print, optional.
        artist (CharField): The artist of the product.
        price (DecimalField): The price of the product.
        rating (DecimalField): The rating of the product, optional.
        image_url (URLField): The URL of the product's image, optional.
        image (ImageField): An uploaded image of the product, optional.
    """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    is_print = models.BooleanField(default=False, null=True, blank=True)
    artist = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """ Returns the name of the product."""
        return self.name
