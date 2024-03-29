from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model

User = get_user_model()

class PostManager(models.Manager):
    def get_actives(self):
        return super().get_queryset().filter(is_active='True')




class Post(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextField()
    thumbnail = models.ImageField(upload_to='post_image_uploads/')
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(db_default=True, default=True)
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, blank=True, null=True)
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    objects = PostManager()

    def __str__(self):
        return self.title
