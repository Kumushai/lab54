from django.shortcuts import render, redirect, get_object_or_404
from django.utils.http import urlencode
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from webapp.forms import SearchForm, ProductForm
from webapp.models import Category, Product


class ProductListView(ListView):
    template_name = "product/index.html"
    context_object_name = 'products'
    model = Product
    ordering = ["category__title", "title"]
    paginate_by = 5
    paginate_orphans = 1

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search_value'] = self.search_value
        return context

    def get_queryset(self):
        queryset = Product.objects.filter(balance__gt=0)
        if self.search_value:
            queryset = queryset.filter(title__icontains=self.search_value)
        return queryset


def product_add_view(request):
    if request.method == "GET":
        form = ProductForm()
        # categories = Category.objects.all()
        return render(request, "product/create_product.html", {"form": form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            return render(request, "product/create_product.html", {"form": form})


def product_view(request, *args, pk, **kwargs):
    product = get_object_or_404(Product, id=pk)
    return render(request, "product/product.html", {"product": product})


def product_update_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == "GET":
        form = ProductForm(instance=product)
        return render(request, "product/update_product.html", {"form": form})
    else:
        form = ProductForm(instance=product, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_view", pk=product.pk)
        else:
            return render(request, "product/update_product.html", {"form": form})


def product_delete_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == "GET":
        return render(request, "product/delete_product.html", {"product": product})
    else:
        product.delete()
        return redirect("index")


def category_add_view(request):
    if request.method == "GET":
        return render(request, "product/create_category.html")
    else:
        Category.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description")
        )
        return redirect("index")
