from django.shortcuts import render
from django.conf import settings

# Create your views here.


def courses(request):

    
    context = {
        'api_key': settings.GOOGLE_MAP_API_KEY,
    }

    return render(request, 'courses/courses.html')

