from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    """
    Model for courses
    """
    excerpt = models.TextField(max_length=30, default='some string')
    name = models.CharField(max_length=254)
    excerpt = models.TextField(max_length=50, default='some string')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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