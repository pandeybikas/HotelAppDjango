from django.db import models

# Create your models here.
class Cafe(models.Model):
    cafe_name = models.CharField(max_length=100, null=True)
    cafe_image = models.ImageField(upload_to='media', null=True)
    address= models.TextField(null=True)
    about =models.TextField(null=True)
    speciality = models.CharField(max_length=100, null=True, choices=(
                                ('', 'Choose feature'),
                                ('Ambient', 'Ambient'),
                                ('Food', 'Food'),
                                ('Location', 'Location'),
                                ('Hospitality', 'Hospitality')
    ))
    feeder_name = models.CharField(max_length=120, null=True)

    def __str__(self):
        return self.cafe_name