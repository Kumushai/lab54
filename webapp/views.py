from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import SearchForm, ProductForm
from webapp.models import Category, Product


def products_list_view(request):
    if request.method == "GET":
        search_form = SearchForm(request.GET)
        product = Product.objects.filter(balance__gt=0).order_by("category", "title")

        if search_form.is_valid():
            product_title = search_form.cleaned_data["product_title"]
            product = product.filter(title__icontains=product_title)
        form = ProductForm()
        context = {"products": product, "form": form, "search_form": search_form}
        return render(request, "index.html", context)
    else:
        return product_add_view(request)


def product_add_view(request):
    if request.method == "GET":
        form = ProductForm()
        # categories = Category.objects.all()
        return render(request, "create_product.html", {"form": form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            return render(request, "create_product.html", {"form": form})


def product_view(request, *args, pk, **kwargs):
    product = get_object_or_404(Product, id=pk)
    return render(request, "product.html", {"product": product})


def product_update_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == "GET":
        form = ProductForm(instance=product)
        return render(request, "update_product.html", {"form": form})
    else:
        form = ProductForm(instance=product, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_view", pk=product.pk)
        else:
            return render(request, "update_product.html", {"form": form})


def product_delete_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == "GET":
        return render(request, "delete_product.html", {"product": product})
    else:
        product.delete()
        return redirect("index")


def category_add_view(request):
    if request.method == "GET":
        return render(request, "create_category.html")
    else:
        Category.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description")
        )
        return redirect("index")
