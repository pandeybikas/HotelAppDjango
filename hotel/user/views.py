from django.shortcuts import render,redirect
from .forms import SignUpForm, ProfileModelForm
from django.contrib.auth import login, logout, authenticate
from .models import Profile
from booking.models import Booking
from django.contrib.auth.decorators import login_required
# Create your views here.
def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form' : form
    }
    return render(request, 'register.html', context)

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def signout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login') 
def profilePage(request):
    
    myTrip = Booking.objects.filter(booker= request.user.id)
    
    context = {
        'myTrip' : myTrip
    }
    return render(request, 'profile.html',context)
@login_required(login_url='login') 
def editProfile(request, pk):
    edit_inst = Profile.objects.get(id = pk)
    editform = ProfileModelForm()
    if request.method == 'POST':
        editform = ProfileModelForm(request.POST, request.FILES, instance=edit_inst)
        if editform.is_valid():
            editform.save()
            return redirect('profile')
    else:
        editform= ProfileModelForm(instance=edit_inst)
    context= {
        'editform' : editform
    }
    return render(request, 'edit-profile.html', context)

    