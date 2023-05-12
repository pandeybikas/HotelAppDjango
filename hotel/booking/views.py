from django.shortcuts import render, redirect
from .models import Booking

def booking(request):
    if request.method == 'POST':
        # bookform = ProfileModelForm(request.POST)
        # if bookform.is_valid():
            # bookform.data['booker'] = request.user
             #bookform.save()
             #return redirect('profile')
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        guest = request.POST.get('guest')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        booker = request.user
        book = Booking(fullname=fullname, email=email, guest=guest, check_in=check_in, check_out=check_out, booker=booker)
        
        book.save()
        return redirect('profile')
     #bookform = ProfileModelForm()
    return render(request, 'booking.html')
