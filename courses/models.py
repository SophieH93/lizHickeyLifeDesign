from django.db import models
from django.contrib.auth.models import User



class Course(models.Model):
    """
    Model for courses
    """
 #   category = models.ForeignKey('Course', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   # subject = models.CharField(max_length=60, null=False, blank=False)
    review = models.TextField(null=False, blank=False)
    rate = models.IntegerField(default=1)

    def __str__(self):
        return self.review