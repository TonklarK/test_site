from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    age =models.IntegerField()
    def __str__(self):
        return f"{self.name} {self.lastname}"


class Post(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100,null=True,blank=True)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    featured_pic = models.ImageField(upload_to="featured-images/",null=True,blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    #num = models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.subject