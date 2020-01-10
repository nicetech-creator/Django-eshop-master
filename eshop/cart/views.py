from django.shortcuts import render
from . import cart
# Create your views here.
def show_cart(request, template_name="cart.html"):
    cart_item_count = cart.cart_distinct_item_count(request)
    cart_items = cart.get_cart_items(request)
    page_title = 'Shopping Cart'
    return render(request, template_name=template_name, context = locals())

