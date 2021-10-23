from django.db import models

# Create your models here.


#Category Model

from django.utils.html import format_html
from django.contrib.auth.models import User
from django.utils.timezone import now



class Category(models.Model):
    cat_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    url=models.CharField(max_length=100)
    image=models.ImageField(upload_to='category/')
    add_date=models.DateTimeField(auto_now_add=True,null=True)


    def imageTag(self):
        return format_html("<img src ='/media/{}'style='width:50px;height:50px;border-radius:50%;'/>".format(self.image))
    def __str__(self):
        return self.title


#Post Model
class Post(models.Model):


    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=150)
    content=models.TextField()
    url=models.CharField(max_length=100)
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)
    img=models.ImageField(upload_to="post/")
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def imageTag(self):
        return format_html("<img src ='/media/{}'style='width:50px;height:50px;border-radius:50%;'/>".format(self.img))
    def __str__(self):
        return self.title




class BlogComment(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(default=now)

