from django.urls import path
from .import views

urlpatterns = [
    path('', views.courses, name='courses'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('add/', views.add_course, name='add_course'),
    path('<course_id>', views.add_review, name='add_review'),
]
