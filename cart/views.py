from django.shortcuts import render, redirect

# Create your views here.

def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    print_type = None
    if 'print_paper' in request.POST:
        print_type = request.POST['print_paper']
    cart = request.session.get('cart', {})

    if print_type:
        if item_id in list(cart.keys()):
            if print_type in cart[item_id]['items_by_print'].keys():
                cart[item_id]['items_by_print'][print_type] += quantity
            else:
                cart[item_id]['items_by_print'][print_type] = quantity
        else:
            cart[item_id] = {'items_by_print': {print_type: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)
