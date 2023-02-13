from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    blog_user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile_user")
    mobile_number= models.IntegerField(default=0)
    is_blogger= models.BooleanField(default=False)
    
    profile_pic = models.ImageField(
        upload_to='static/profile_pic', null=True, default='user.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.blog_user.username}'
    
    
class Category(models.Model):
    category_name = models.CharField(max_length=255,null=False)
    is_show= models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.category_name
    
class Blog(models.Model):
    category= models.ForeignKey(Category, on_delete=models.CASCADE,related_name="blog_category")
    title = models.CharField(max_length=255)
    description = models.TextField()
    blogger= models.ForeignKey(User, on_delete=models.CASCADE)
    is_post_show = models.BooleanField(default=True)
    is_comments_show= models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.title


class BlogImages(models.Model):
    blog= models.ForeignKey(Blog, on_delete=models.CASCADE,related_name="img_blog")
    img_name = models.CharField(max_length=255)
    image= models.ImageField(
        upload_to='static/blogs_images/', null=True)
    is_show = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.img_name
    
    
class Like(models.Model):
    like_blog= models.ForeignKey(Blog, on_delete=models.CASCADE,related_name="like_blog")
    like_user= models.ForeignKey(User, on_delete=models.CASCADE,related_name="like_user")
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return self.blog
    
class Comment(models.Model):
    
    comment_blog= models.ForeignKey(Blog, on_delete=models.CASCADE,related_name="comment_blog")
    comment_user= models.ForeignKey(User, on_delete=models.CASCADE,related_name="comment_user")
    comment_msg= models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return self.comment_msg
    
    
@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        person=Profile.objects.create(blog_user=instance)
        person.save()
        
