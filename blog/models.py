from django.db import models
from django.contrib.auth.models import User
from cloudinary.model import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = 