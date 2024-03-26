from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def cart_contents(request):
    """
    Calculate and return the cart contents context.
    Processes the cart items stored in the session, calculating the total cost,
    delivery cost, and grand total. It also counts the total number of items.
    Supports products with variations, such as different print types.

    Parameters:
    - request (HttpRequest): The HttpRequest object.

    Returns:
    - context (dict): Context dictionary containing cart details and grand total.
    """
    cart_items = []
    total = Decimal('0')
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * Decimal(product.price)
            product_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
            # Minor custom adjustment by adding print_type
        else:
            product = get_object_or_404(Product, pk=item_id)
            for print_type, quantity in item_data['items_by_print'].items():
                total += quantity * Decimal(product.price)
                product_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'print_type': print_type,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context