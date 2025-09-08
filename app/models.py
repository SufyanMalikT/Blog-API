from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.utils.text import slugify
# Create your models here.

class CustomUser(AbstractUser):
    pass

class Blog(models.Model):
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=100,blank=True,null=True)
    slug = models.SlugField(blank=True,null=True)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser,related_name="blog",on_delete=models.CASCADE)
    img = models.ImageField(upload_to='blog/img/',blank=True,null=True)

    def save(self,*args,**kwargs):
        print('this is the models save function.')
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)
    

    def __str__(self):
        return f"{self.title} - {self.author.username}"


class Comment(models.Model):
    author = models.ForeignKey(CustomUser,related_name='comments',on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,related_name='comments',on_delete=models.CASCADE)
    content = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} commented on {self.blog.title}"
    
class Like(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='likes')
    blog = models.ForeignKey(Blog,related_name="likes",on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user','blog')

    def __str__(self):
        return f"{self.user.username} liked {self.blog.author.username}'s Blog."

