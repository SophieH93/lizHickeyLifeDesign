from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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

@login_required
def add_course(request):
    """ Add a course to the website as a superuser"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added course!')
            return redirect(reverse('courses'))
        else:
            messages.error(request, 'Failed to add course. Please ensure the form is valid.')
    else:
        form = CourseForm()

    template = 'courses/add_course.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_course(request, course_id):
    """ Edit a course in the website as a superuser """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated course!')
            return redirect(reverse('course_detail', args=[course.id]))
        else:
            messages.error(request, 'Failed to update course. Please ensure the form is valid.')
    else:
        form = CourseForm(instance=course)
        messages.info(request, f'You are editing {course.name}')

    template = 'courses/edit_course.html'
    context = {
        'form': form,
        'course': course,
    }

    return render(request, template, context)

@login_required
def delete_course(request, course_id):
    """ Delete a course from the website as a superuser """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
        
    course = get_object_or_404(Course, pk=course_id)
    course.delete()
    messages.success(request, 'course deleted!')
    return redirect(reverse('courses'))


def add_review(request, course_id):

    if request.method == 'POST': 
      review_form = ReviewForm(request.POST)
      if review_form.is_valid():
        review_form.save()
        messages.success(request, "Your review has ben sent. Thank you for your interest.")
        print('shit')
        return redirect(reverse('course_detail'))

    return redirect(reverse('course_detail'))

