from django import forms 
from .models import Cafe

class CafeModelForm(forms.ModelForm):

    cafe_name = forms.CharField(
        label= 'Cafe Name',
        max_length= 25,
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Zizou cafe',
            'type' : 'text'
        })
    )
    address = forms.CharField(
        label= 'Cafe Address',
        
        widget= forms.Textarea(attrs={
            'class' : 'form-control',
            'placeholder' : 'Canought palace-New Delhi',
            'rows' : 5,
            
        })
    )
    about = forms.CharField(
        label= 'About Cafe',
        
        widget= forms.Textarea(attrs={
            'class' : 'form-control',
            'placeholder' : 'great place....',
            'rows' : 5,
            
        })
    )
    Special = (
        ('', 'Choose feature'),
        ('Ambient', 'Ambient'),
        ('Food', 'Food'),
        ('Location', 'Location'),
        ('Hospitality', 'Hospitality')
    )
    speciality = forms.CharField(
        label= 'Cafe Speciality',
        
        widget= forms.Select(attrs={
            'class' : 'form-control',
            'placeholder' : 'Food',
            
            
        }, choices=Special)
    )
    cafe_image = forms.FileField(
        label= 'Upload Cafe Image',
        widget= forms.FileInput(attrs={
            'accept' : 'image/png, image/jpeg',
            'class' : 'form-control'
        })
    )
    feeder_name = forms.CharField(
        label= 'Your Name',
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'john doe'
        })
    )
    class Meta:
        model = Cafe
        fields = ['cafe_name', 'address', 'about','speciality', 'cafe_image', 'feeder_name']