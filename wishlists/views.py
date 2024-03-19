from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile
from products.models import Product
from .models import Wishlist, WishlistItem

@login_required
def user_wishlists(request):
    """ List all the wishlists associated with the currently logged-in user """
    user_profile = UserProfile.objects.get(user=request.user)
    try:
        wishlist = Wishlist.objects.get(user=user_profile)
        wishlist_items = WishlistItem.objects.filter(wishlist=wishlist)
    except Wishlist.DoesNotExist:
        wishlist_items = None


    context = {
        'wishlist_items': wishlist_items,
    }

    return render(request, 'wishlists/wishlists.html', context)


@login_required
def add_to_wishlist(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    user_profile = UserProfile.objects.get(user=request.user)
    wishlist, created = Wishlist.objects.get_or_create(user=user_profile)
    if WishlistItem.objects.filter(wishlist=wishlist, product=product).exists():
        messages.info(request, 'The product is already in your wishlist.')
    else:
        WishlistItem.objects.create(wishlist=wishlist, product=product)
        messages.success(request, 'Product added to wishlist.')
    return redirect('product_detail', product_id=item_id)


@login_required
def remove_from_wishlist(request, item_id):
    wishlist_item = get_object_or_404(WishlistItem, pk=item_id)
    wishlist_item.delete()
    messages.success(request, 'Product removed from wishlist')
    return redirect('wishlists:user_wishlists')

@login_required
def add_wish_to_cart(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    cart = request.session.get('cart', {})

    item_id_str = str(item_id)

    if item_id_str in cart:
        cart[item_id_str] += quantity
        messages.success(request, f'Updated {product.name} quantity to {cart[item_id_str]}')
    else:
        cart[item_id_str] = quantity
        messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    return redirect('wishlists:user_wishlists')