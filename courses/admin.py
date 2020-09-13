from django.contrib import admin
from .models import Course, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'price',
        'image',
    )

    ordering = ('sku',)

class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ('course', 'review')


admin.site.register(Course, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
