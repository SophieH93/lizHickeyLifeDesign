from django.db import models
from courses.models import Course


class Reviews(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)    
    review = models.TextField(null=False, blank=False)
    RATING_CHOICES = (
        (0, 'No rating'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    rate = models.IntegerField(choices=RATING_CHOICES, default=0)
    
    def __str__(self):
        return self.review