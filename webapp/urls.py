from django.urls import path

from webapp.views.product_views import product_view, category_add_view,\
    product_delete_view, product_update_view, ProductListView, ProductCreateView

urlpatterns = [
    path('', ProductListView.as_view(), name="index"),
    path('products/', ProductListView.as_view(), name="products_list"),
    path('products/add/', ProductCreateView.as_view(), name="product_add"),
    path('product/<int:pk>/', product_view, name="product_view"),
    path('product/<int:pk>/update/', product_update_view, name="product_update_view"),
    path('product<int:pk>/delete/', product_delete_view, name="product_delete_view"),
    path('category/add/', category_add_view, name="category_add")
]


