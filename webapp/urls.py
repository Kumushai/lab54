from django.urls import path

from webapp.views.product_views import category_add_view,\
    ProductDeleteView, ProductListView, ProductCreateView, ProductUpdateView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name="index"),
    path('products/', ProductListView.as_view(), name="products_list"),
    path('products/add/', ProductCreateView.as_view(), name="product_add"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="product_view"),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name="product_update_view"),
    path('product<int:pk>/delete/', ProductDeleteView.as_view(), name="product_delete_view"),
    path('category/add/', category_add_view, name="category_add")
]


