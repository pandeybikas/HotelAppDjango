from django.contrib import admin
from .models import Hotel, Location, Menu, Amminities
# Register your models here.
class HotelModelAdmin(admin.ModelAdmin):
    list_display = ['hotel_name', 'price', 'location']
    prepopulated_fields = {'slug' : ['hotel_name',]}
class LocationAdmin(admin.ModelAdmin):
    list_display = ['city_name']
    prepopulated_fields = {'slug' : ('city_name',)}
admin.site.register(Hotel, HotelModelAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Menu)
admin.site.register(Amminities)
