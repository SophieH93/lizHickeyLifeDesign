from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.conf import settings
from .models import Course, Review
from .forms import ReviewForm, CourseForm


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
    A view to display an individula course information & Review form
    """
    course = get_object_or_404(Course, pk=course_id)
    review_form = ReviewForm()
    reviews = Review.objects.filter(course_id=course_id)

    context = {
        'course': course,
        'review_form': review_form,
        'reviews': reviews,

    }

    return render(request, 'courses/course_detail.html', context)


def add_course(request):
    """ Add a course to the store """
    form = CourseForm()
    template = 'courses/add_course.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def add_review(request, course_id):

    if request.method == 'POST': 
      review_form = ReviewForm(request.POST)
      if review_form.is_valid():
        review_form.save()
        messages.success(request, "Your review has ben sent. Thank you for your interest.")
        print('shit')
        return redirect(reverse('course_detail'))

    return redirect(reverse('course_detail'))

