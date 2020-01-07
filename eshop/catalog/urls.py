from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    # post views
    path('', views.index, name='post_list'),
   
]
