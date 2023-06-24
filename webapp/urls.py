from django.urls import path

from webapp.views import products_list_view, product_view, product_add_view, category_add_view

urlpatterns = [
    path('', products_list_view, name="index"),
    path('products/', products_list_view, name="products_list"),
    path('products/add/', product_add_view, name="product_add"),
    path('product/<int:pk>/', product_view, name="product_view"),
    path('category/add/', category_add_view, name="category_add")
]