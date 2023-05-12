from django import forms 
from .models import Menu, Hotel
from booking.models import Booking
class MenuModelForm(forms.ModelForm):
    item = forms.CharField(
        label= 'Item Name',
        max_length= 30,
        min_length= 2,
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'style' : 'font-size: 14px;',
            'type': 'text',
            'placeholder' : 'dish name...'
        })
    )
    price = forms.CharField(
        label= 'Item Price',
        
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'style' : 'font-size: 14px;',
            'type': 'number',
            'placeholder' : '₹...'
        })
    )
    pic = forms.FileField(
        label= 'Upload Image',
        
        
        widget= forms.FileInput(attrs={
            'class' : 'form-control',
            'style' : 'font-size: 14px;',
            'accept' : 'image/png, image/jpeg',
            'placeholder' : '₹...'
        })
    )
    class Meta:
        model = Menu
        fields = '__all__'
        exclude = ['hotel']

class BookModelForm(forms.ModelForm):
    fullname = forms.CharField(
        label= 'Full Name',
        max_length= 35,
        min_length= 2,
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'enter name....'
        })
    )
    email = forms.EmailField(
        label= 'Email',
        
        widget= forms.EmailInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'abc@gmail.com',
            'type' : 'email'
        })
    )
    guest = forms.CharField(
        label= 'No. of guest',
        
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : '0-10',
            'type' : 'number'
        })
    )
    check_in = forms.DateField(
        label= 'Check-In Date',
        
        widget= forms.DateInput(attrs={
            'class' : 'form-control',
            
            'type' : 'date'
        })
    )
    check_out = forms.DateField(
        label= 'Check-Out Date',
        
        widget= forms.DateInput(attrs={
            'class' : 'form-control',
            
            'type' : 'date'
        })
    )
    class Meta:
        model = Booking
        field = ['fullname', 'email', 'guest', 'check_in', 'check_out']
        exclude = ['booker', 'hotel']
    