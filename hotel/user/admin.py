from django.contrib import admin
from .models import Profile
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ['user','fullName', 'image','phone', 'address']
admin.site.register(Profile,ProfileAdmin)