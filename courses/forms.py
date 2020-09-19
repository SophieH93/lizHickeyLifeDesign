from django import forms
from .models import Review, Course


class CourseForm(forms.ModelForm):
    """
    Form to add a course for superusers only
    """
    class Meta:
        model = Course
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['course', 'review'] 

