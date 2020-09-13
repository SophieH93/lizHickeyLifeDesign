from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Course
from .forms import ReviewForm



def courses(request):
    """
    A view to display all courses & google map api
    """
    courses = Course.objects.all()

    context = {
        'courses': courses,
        'api_key': settings.GOOGLE_MAP_API_KEY,
    }

    return render(request, 'courses/courses.html', context)


def course_detail(request, course_id):
    """
    A view to display an individula course information
    """
    course = get_object_or_404(Course, pk=course_id)
    review_form = ReviewForm()

    context = {
        'course': course,
        'review_form': review_form,

    }

    return render(request, 'courses/course_detail.html', context)

