from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Category, Product


def products_list_view(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "index.html", context)


def product_add_view(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, "create_product.html", {"categories": categories})
    else:
        product = Product.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            category_id=request.POST.get("category_id"),
            price=request.POST.get("price"),
            image=request.POST.get("image")
        )
        return redirect("product_view", pk=product.pk)


def product_view(request, *args, pk, **kwargs):
    product = get_object_or_404(Product, id=pk)
    return render(request, "product.html", {"product": product})


def category_add_view(request):
    if request.method == "GET":
        return render(request, "create_category.html")
    else:
        Category.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description")
        )
        return redirect("index")
