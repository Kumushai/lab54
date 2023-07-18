from django.shortcuts import render, redirect, get_object_or_404

from django.views import View
from django.views.generic import FormView

from webapp.forms import OrderForm
from webapp.models import Product, Cart, Order, OrderProduct


class AddToCartView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        if product.balance > 0:
            cart, created = Cart.objects.get_or_create(product=product)
            if cart.quantity < product.balance:
                cart.quantity += 1
                cart.save()

        return redirect('index')


class CartView(FormView):
    template_name = 'cart/cart.html'
    form_class = OrderForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_items_with_total'] = [(cart_item, cart_item.product.price * cart_item.quantity)
                                            for cart_item in self.get_cart_items()]
        return context

    def get(self, request):
        cart_items = Cart.objects.select_related('product')
        print(cart_items)
        total = sum(cart_item.product.price * cart_item.quantity for cart_item in cart_items)
        print(total)

        cart_items_with_total = [(cart_item, cart_item.product.price * cart_item.quantity) for cart_item in cart_items]
        print(cart_items_with_total)
        return render(request, 'cart/cart.html', {'cart_items_with_total': cart_items_with_total, 'total': total})

    def form_valid(self, form):
        order = Order.objects.create(
            name=form.cleaned_data['name'],
            phone=form.cleaned_data['phone'],
            address=form.cleaned_data['address']
        )
        cart_items = self.get_cart_items()
        for cart_item in cart_items:
            OrderProduct.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity
            )

        return super().form_valid(form)


class CreateOrderView(View):
    def post(self, request):
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']

        order = Order.objects.create(name=name, address=address, phone=phone)

        cart_items = Cart.objects.all()
        for cart_item in cart_items:
            order.products.add(cart_item.product, through_defaults={'quantity': cart_item.quantity})

        cart_items.delete()
        return redirect('cart')


class RemoveFromCartView(View):
    def post(self, request, pk):
        cart_item = get_object_or_404(Cart, pk=pk)
        cart_item.delete()

        return redirect('cart')