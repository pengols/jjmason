from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class BlogPost(models.Model):
    post_title = models.CharField(max_length=150, unique=True)
    post_slug = models.SlugField(max_length=150, unique=True)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='blog_posts')
    post_updated = models.DateTimeField(auto_now=True)
    post_content = models.TextField()
    post_created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image_url = models.URLField(max_length=1024,
                                null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['-post_created']

    def __str__(self):
        return self.post_title
