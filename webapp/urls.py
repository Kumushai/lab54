from django.urls import path

from webapp.views import products_list_view, product_view, product_create_view

urlpatterns = [
    path('', products_list_view, name="index"),
    path('products/add/', product_create_view, name="product_add"),
    path('product/<int:pk>/', product_view, name="product_view")
]