from django.db import models

# Create your models here.
class Location(models.Model):
    city_name= models.CharField(max_length=100, null=True)
    slug = models.SlugField(null=True)
    pic= models.ImageField(upload_to='media', null=True)
    bio = models.TextField()
    def __str__(self):
        return self.city_name


    
class Amminities(models.Model):
    name= models.CharField(max_length=100, null=True)
    icon = models.ImageField(upload_to='media')
    def __str__(self):
        return self.name





class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100, null=True)
    slug = models.SlugField(null=True)
    price = models.PositiveIntegerField( null=True)
    desc = models.TextField(null=True)
    
    image = models.ImageField(upload_to='media')
    location = models.ForeignKey(Location, on_delete=models.PROTECT, null= True)
    amminity = models.ManyToManyField(Amminities)
    
    
    
    def __str__(self):
        return self.hotel_name

class Menu(models.Model):
    item= models.CharField(max_length=100, null=True)
    price = models.CharField(max_length=100, null=True)
    pic= models.ImageField(upload_to='media', null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, related_name='hotels')
    def __str__(self):
        return self.item