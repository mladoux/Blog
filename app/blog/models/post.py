from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):

    title       = models.CharField(max_length=255, unique=True)
    slug        = models.SlugField(max_length=255, unique=True)
    author      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content     = models.TextField()
    created_on  = models.DateTimeField(auto_now_add=True)
    updated_on  = models.DateTimeField(auto_now=True)
    publish_on  = models.DateTimeField(default=timezone.now)
    status      = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-publish_on']
    
    def __str__(self):
        return self.title
