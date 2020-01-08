from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    # post views
    path('', views.show_cart, name='cart'),
]
