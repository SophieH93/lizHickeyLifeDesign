from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from courses.models import Course


def shopping_cart(request):
    """
    Display users shopping cart.
    """
    return render(request, 'shopping_cart/shopping_cart.html')


def add_to_cart(request, item_id):
    """
    Add course to the cart.
    """
    course = Course.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {course.name} to cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """
    Remove course from the cart.
    """
    try:
        cart = request.session.get('cart', {})
        course = get_object_or_404(Course, pk=item_id)
        cart.pop(item_id)
        messages.info(request, f"Removed {course.name} from your cart.")
        request.session['cart'] = cart
        return redirect('shopping_cart')

    except Exception as e:
        return HttpResponse(status=500)

