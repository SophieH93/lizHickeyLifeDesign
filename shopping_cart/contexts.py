from courses.models import Course


def cart_contents(request):

    cart_items = []
    total = 0
    course_count = 0

    context = {
        'cart_items' : cart_items,
        'total': total,
        'course_count' : course_count,
    }

    return context
