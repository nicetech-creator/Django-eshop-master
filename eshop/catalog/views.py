from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from .models import Category, Product
from cart import cart
from django.http import JsonResponse

# Create your views here.
def index(request, template_name="index.html"):
    categories = Category.objects.all()
    products = Product.objects.all()
    page_title = 'E-Shop Master'
    return render(request, template_name=template_name, context = locals())

def show_category(request, category_slug, template_name="category.html"):
    c = get_object_or_404(Category, slug=category_slug)
    products = c.product_set.all()
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description
    return render(request, template_name=template_name, context = locals())

def show_product(request, product_slug, template_name="product.html"):
    p = get_object_or_404(Product, slug=product_slug)
    categories = p.categories.filter(is_active=True)
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    if request.method == 'POST':
        cart.add_to_cart(request)
        data = {
            'message': 'added successfully',
        }
        return JsonResponse(data)
    else:
        return render(request, template_name=template_name, context = locals())