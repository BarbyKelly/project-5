# How To ... base from PP4 Blog: https://github.com/BarbyKelly/blog/blob/main/resources/models.py
from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))


# 'How to ...' model
class HowTo(models.Model):
    """
    Fields for 'How To...' page
    """
    title = models.CharField(max_length=150, unique=True)
    content = models.TextField()
    resource_url = models.URLField(null=False, blank=False)
    shared_on = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["title"]
    
    def __str__(self):
        return self.title
