from django.shortcuts import render
from django.conf import settings


def testimonials(request):

    context = {
        'api_key': settings.GOOGLE_MAP_API_KEY,
    }

    return render(request, 'testimonials/testimonials.html', context)



