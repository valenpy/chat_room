from django.db import models

from .utils import get_slug


class Message(models.Model):
    msg_text = models.TextField()
    author = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = get_slug(self.author)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.author}"
