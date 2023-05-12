from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from .models import Profile
class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label= 'Username',
        max_length= 8,
        min_length= 2,
        error_messages= {'required' : 'This field cannot be empty !'},
        widget= forms.TextInput(attrs= {
            'placeholder' : 'type username...',
            'class' : 'form-control',
            'style' : 'font-size: 14px;'
        })
    )
    email = forms.EmailField(
        label= 'Email',
       
        error_messages= {'required' : 'This field cannot be empty !'},
        widget= forms.EmailInput(attrs= {
            'placeholder' : 'type email address ...',
            'class' : 'form-control',
            'style' : 'font-size: 14px;'
        })
    )
    password1 = forms.CharField(
        label= 'Password',
       
        error_messages= {'required' : 'This field cannot be empty !'},
        widget= forms.PasswordInput(attrs= {
            'placeholder' : 'type password ...',
            'class' : 'form-control',
            'style' : 'font-size: 14px;'
        })
    )
    password2 = forms.CharField(
        label= 'Confirm Password',
       
        error_messages= {'required' : 'This field cannot be empty !'},
        widget= forms.PasswordInput(attrs= {
            'placeholder' : 're-type password ...',
            'class' : 'form-control',
            'style' : 'font-size: 14px;'
        })
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileModelForm(forms.ModelForm):
    fullName = forms.CharField(
        label= 'Full Name',
        max_length= 25,
        min_length= 3,
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'style' : 'font-size: 14px;',
            'placeholder' : 'type your name...'
        })
    )
    phone = forms.CharField(
        label= 'Phone',
        max_length= 11,
        min_length= 5,
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'style' : 'font-size: 14px;',
            'type' : 'number',
            'placeholder' : 'type your phone number...'
        })
    )
    address = forms.CharField(
        label= 'Address',
        max_length= 50,
        min_length= 3,
        widget= forms.Textarea(attrs={
            'class' : 'form-control',
            'style' : 'font-size: 14px;',
            'rows' : 5,
            'placeholder' : 'type your address...'
        })
    )
    image = forms.FileField(
        label= 'Upload Image',
        
        widget= forms.FileInput(attrs={
            'class' : 'form-control',
            'style' : 'font-size: 14px;',
            'accept' : 'image/jpeg, image/png',
            
        })
    )
    class Meta:
        model = Profile
        fields = ['fullName', 'phone', 'address', 'image']
        exclude = ['user']