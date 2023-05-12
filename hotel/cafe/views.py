from django.shortcuts import render, redirect
from .forms import CafeModelForm
from .models import Cafe
from django.contrib.auth.decorators import login_required
# Create your views here.
def cafelist(request):
    all_cafe = Cafe.objects.all()
    context = {
        'all_cafe' : all_cafe
    }
    return render(request, 'cafe-list.html', context)
@login_required(login_url='login')
def addCafe(request):
    form = CafeModelForm()
    if request.method == "POST":
        form = CafeModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context ={
        'form' : form
    }
    return render(request, 'add-cafe.html', context)