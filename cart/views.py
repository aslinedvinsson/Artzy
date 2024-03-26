from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from products.models import Product


def view_cart(request):
    """ A view that renders the cart contents page """
    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """Adds a product quantity to the shopping cart."""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    print_type = request.POST.get('print_paper', None)
    cart = request.session.get('cart', {})

    if print_type:
        cart.setdefault(item_id, {'items_by_print': {}}).setdefault(
            'items_by_print', {}).setdefault(print_type, 0)
        cart[item_id]['items_by_print'][print_type] += quantity
        message = f'Updated print {print_type} {product.name} quantity to {cart[item_id]["items_by_print"][print_type]}' if print_type in cart[item_id]['items_by_print'
            ] else f'Added print {print_type} {product.name} to your cart'
    else:
        cart[item_id] = cart.get(item_id, 0) + quantity
        message = f'Updated {product.name} quantity to {cart[item_id]}' if item_id in cart else f'Added {product.name} to your cart'

    messages.success(request, message, extra_tags='cart')
    request.session['cart'] = cart
    return redirect('cart:view_cart')

def adjust_cart(request, item_id):
    """Adjusts the quantity of the specified product."""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    print_type = request.POST.get('print_paper', None)
    cart = request.session.get('cart', {})

    if print_type:
        if quantity > 0:
            cart[item_id]['items_by_print'][print_type] = quantity
        else:
            del cart[item_id]['items_by_print'][print_type]
            if not cart[item_id]['items_by_print']:
                del cart[item_id]
        message = f'Updated print {print_type} {product.name} quantity to {cart[item_id]["items_by_print"][print_type]}' if quantity > 0 else f'Removed print {print_type} {product.name} from your cart'
    else:
        if quantity > 0:
            cart[item_id] = quantity
        else:
            del cart[item_id]
        message = f'Updated {product.name} quantity to {cart[item_id]}' if quantity > 0 else f'Removed {product.name} from your cart'

    messages.success(request, message, extra_tags='cart')
    request.session['cart'] = cart
    return redirect(reverse('cart:view_cart'))

def remove_from_cart(request, item_id):
    """Removes the item from the shopping cart."""
    try:
        product = get_object_or_404(Product, pk=item_id)
        print_type = request.POST.get('print_paper', None)
        cart = request.session.get('cart', {})

        if print_type:
            del cart[item_id]['items_by_print'][print_type]
            if not cart[item_id]['items_by_print']:
                del cart[item_id]
        else:
            del cart[item_id]

        messages.success(request, f'Removed {product.name} from your cart', extra_tags='cart')
        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)