from django.shortcuts import get_object_or_404
from courses.models import Course


def cart_contents(request):

    cart_items = []
    total = 0
    course_total = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        course = get_object_or_404(Course, pk=item_id)
        total += quantity * course.price
        course_total += quantity * course.price
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'course': course,
        })

    context = {
        'cart_items': cart_items,
        'total': total,
        'course_total': course_total,
    }

    return context
