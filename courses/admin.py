from django.contrib import admin
from .models import Course, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'image',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'course',
        'user',
        'review',
        'rate',
    )


admin.site.register(Course, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
