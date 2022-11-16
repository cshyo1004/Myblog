from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='post_image', default='base.jpg')

    def __str__(self):
        return self.title