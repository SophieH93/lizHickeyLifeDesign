from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    status = models.CharField(max_length=10,  choices=options, default='draft')
    objects = models.Manager()
    newmanager = NewManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

