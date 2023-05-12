from django import forms 
from .models import Blog, Comment

class BlogModelForm(forms.ModelForm):
    
    title = forms.CharField(
        label= 'Story Title',
        max_length= 80,
        min_length= 2,
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'title...'
            
        })
    )
    desc = forms.CharField(
        label= 'Full Story',
        min_length= 50,
        max_length= 1500,
        widget= forms.Textarea(attrs={
            'rows' : 10,
           
            'placeholder' : 'start writing...',
            'class' : 'form-control'
        })

    )
    image = forms.FileField(
        label= 'Featured Image',
        widget= forms.FileInput(attrs={
            'accept' : 'image/png, image/jpeg',
            'class' : 'form-control'
        })
    )
    author = forms.CharField(
        label= 'Author Name',
        max_length= 30,
        min_length= 2,
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'name....'
            
        })
    )
    author_bio = forms.CharField(
        label= 'About Author',
        min_length= 50,
        max_length= 1500,
        widget= forms.Textarea(attrs={
            'rows' : 10,
           
            'placeholder' : 'few lines about yourself...',
            'class' : 'form-control'
        })

    )
    author_pic = forms.FileField(
        label= 'Author Display Image',
        widget= forms.FileInput(attrs={
            'accept' : 'image/png, image/jpeg',
            'class' : 'form-control'
        })
    )
    publish_date = forms.DateField(
        label= 'Publish Date',
        widget= forms.DateInput(attrs={
            'type' : 'date'
        })
    )
    class Meta:
        model = Blog
        fields = ['title', 'desc', 'image',  'tag', 'author', 'author_bio', 'author_pic', 'publish_date']
        exclude= ['approved', 'slug']
        labels = {
            'tag' : 'Related Tags'
        }



class CommentModelForm(forms.ModelForm):
    name =  forms.CharField(
        label= 'Your Name',
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'full name'
        })
    )
    body =  forms.CharField(
        label= 'Your Comment',
        widget= forms.Textarea(attrs={
            'class' : 'form-control',
            'placeholder' : 'comment...'
        })
    )
    class Meta:
        model = Comment
        fields = ['name', 'body']
        exclude = ['post', 'date_created']