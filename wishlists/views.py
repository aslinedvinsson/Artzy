from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile
from products.models import Product
from .models import Wishlist, WishlistItem
from .forms import WishlistForm

# Create your views here.

@login_required
def user_wishlists(request):
    """ List all the wishlists associated with the currently logged-in user """
    user_profile = UserProfile.objects.get(user=request.user)
    wishlists = Wishlist.objects.filter(user=user_profile)
    return render(request, 'wishlists/wishlists.html')


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user_profile = UserProfile.objects.get(user=request.user)
    # Use the UserProfile instance to get or create the wishlist
    wishlist, created = Wishlist.objects.get_or_create(user=user_profile)
    WishlistItem.objects.create(wishlist=wishlist, product=product)
    if created:
        messages.success(request, 'Wishlist created and product added.')
    else:
        messages.success(request, 'Product added to wishlist.')
    return redirect('product_detail', product_id=product_id)


@login_required
def remove_from_wishlist(request, wishlist_item_id):
    wishlist_item = get_object_or_404(WishlistItem, pk=wishlist_item_id)
    wishlist_item.delete()
    messages.success(request, 'Product removed from wishlist')
    return redirect('user_wishlists')