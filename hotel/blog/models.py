from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.
Tag = (
    
    ('Mountain', 'Mountain'),
    ('solo trip', 'solo trip'),
    ('family trip', 'family trip'),
    ('Get-Together', 'Get-Together'),
    ('others', 'others')
)

class Blog(models.Model):
    title = models.CharField(max_length=100, null= True)
    slug = models.SlugField(null=True)
    image = models.ImageField(upload_to='media', null=True)
    desc= models.TextField(null=True)
    tag = MultiSelectField(max_length=100, null=True, choices= Tag)
    author = models.CharField(max_length=100, null=True)
    author_bio = models.TextField(null=True)
    author_pic = models.ImageField(upload_to='media', null=True)
    publish_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    approved = models.BooleanField(null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, related_name='comment')
    name = models.CharField(max_length=100, null=True)
    body = models.TextField(null=True)
    date_created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name