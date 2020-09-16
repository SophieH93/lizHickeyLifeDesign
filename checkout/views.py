from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})

    if not cart:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('courses'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HFnRvHiDfU83hDhYlDXWr3BAbSq9x0L44YgVbz4Vq2RL9iUqDKfCKweNcA7vftwrKI5jVghD33fsf3d9bnd0seY00jLyA6ZfT',
        'client_secret': 'test cleint secret',
    }

    return render(request, template, context)

