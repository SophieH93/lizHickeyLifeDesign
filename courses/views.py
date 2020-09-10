from django.shortcuts import render
from django.conf import settings
from .models import Course

# Create your views here.


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

