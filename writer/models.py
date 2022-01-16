from django.db import models

# Create your models here.

class Blogpost(models.Model):
    blog_title = models.CharField(max_length=255)
    blog_content = models.TextField()

