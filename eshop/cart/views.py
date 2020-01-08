from django.shortcuts import render

# Create your views here.
def show_cart(request, template_name="cart.html"):
    cart_item_count = cart.cart_item_count(request)
    page_title = 'Shopping Cart'
    return render(request, template_name=template_name, context = locals())