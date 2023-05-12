from django.db import models
from django.contrib.auth.models import User
from home.models import Hotel
# Create your models here.
class Booking(models.Model):
    booker = models.ForeignKey(User, on_delete=models.PROTECT, null= True)
    fullname= models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    guest = models.CharField(null=True, max_length=100)
    check_in = models.DateField(auto_now=False, auto_now_add=False)
    check_out= models.DateField(auto_now=False, auto_now_add=False)
    hotel = models.ForeignKey(Hotel, on_delete=models.PROTECT, null= True)

    def __str__(self):
        return self.fullname