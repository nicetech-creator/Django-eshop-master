from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    # post views
    path('', views.index, name='index'),
    path('category/<slug:category_slug>', views.show_category, name="catalog_category"),
    path('product/<slug:product_slug>', views.show_product, name="catalog_product"),
]
