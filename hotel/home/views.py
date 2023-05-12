from django.shortcuts import render, redirect
from .models import Hotel, Menu, Location, Amminities
from .forms import MenuModelForm, BookModelForm
from django.contrib.auth.decorators import login_required
from booking.models import Booking
from django.db.models import Q 
from django.core.paginator import Paginator
from cafe.models import Cafe
from blog.models import Blog
from django.urls import reverse
# Create your views here.
def index(request):
    city_obj = Location.objects.all()
    cafe_obj = Cafe.objects.all()
    all_blog = Blog.objects.all()
    all_menu = Menu.objects.raw(" select * from home_menu group by item ")
    page_obj=  Hotel.objects.all()

    paginator = Paginator(page_obj, 3)
    page_number = request.GET.get('page')
    page_obj= paginator.get_page(page_number)
    
    context = {
        
        'page_obj' : page_obj,
        'city_obj' : city_obj,
        'cafe_obj' : cafe_obj,
        'all_blog' : all_blog,
        'all_menu' : all_menu
    }
    return render(request, 'home.html', context)

def hotelList(request):
    hotel_obj = Hotel.objects.all()
    amm_obj = Amminities.objects.all()
    city_obj = Location.objects.all()
    
    query = request.GET.get('search')
    search_amm = request.GET.getlist('amminity')
    search_city = request.GET.getlist('city')
    search_price = request.GET.get('sort_by')
    if query:
        hotel_obj = hotel_obj.filter(Q(hotel_name__icontains=query) | Q(desc__icontains=query))
    if search_amm:
        hotel_obj = Hotel.objects.filter(amminity__name__in= search_amm)   
    if search_city:
        hotel_obj = Hotel.objects.filter(location__city_name__in=search_city)
    if search_price:
        if search_price == 'ASC':
            hotel_obj =Hotel.objects.order_by('price')
        elif search_price == 'DSC':
            hotel_obj= Hotel.objects.order_by('-price')
    
    paginator = Paginator(hotel_obj, 3)
    page_number = request.GET.get('page')
    hotel_obj= paginator.get_page(page_number)
    context={
                
                'query' : query,
                'hotel_obj' : hotel_obj,
                'amm_obj' : amm_obj,
                'search_amm' : search_amm,
                'city_obj' : city_obj,
                'search_city' : search_city,
                'search_price' : search_price
                
            }
    return render(request, 'hotel-list.html', context)



def hotelDetail(request, slug):
    detail_obj = Hotel.objects.get(slug = slug)
    return render(request, 'hotel-detail.html', {'detail_obj' : detail_obj})



def hotelMenu(request, slug):
    menuInst = Hotel.objects.get(slug = slug)
    menuform = MenuModelForm(instance=menuInst)
    if request.method == 'POST':
        menuform = MenuModelForm(request.POST, request.FILES, instance=menuInst)
        if menuform.is_valid():
            item = request.POST.get('item')
            price = request.POST.get('price')
            pic = request.FILES['pic']
            m= Menu(item=item, price=price, pic=pic, hotel=menuInst)
            m.save()
        return redirect(reverse('hotel-detail', args=[menuInst.slug]))
    else:
        menuform = MenuModelForm()
    context = {
        'menuInst' : menuInst, 
        'menuform' : menuform
    }
    return render(request, 'hotel-menu.html', context)

def editMenu(request, pk):
    edit_obj = Menu.objects.get(id = pk)
    if request.method == 'POST':
        form = MenuModelForm(request.POST, request.FILES, instance=edit_obj)
        if form.is_valid():
            form.save()
            return redirect(reverse('hotel-detail', args=[edit_obj.hotel.slug])) 
            #this takes instance created above(edit_obj).refering instance field name(hotel).argument for redirected url(slug)
    else :
        form = MenuModelForm(instance=edit_obj)
    context= {
        'edit_obj' : edit_obj,
        'form' : form
    }
    return render(request, 'edit-menu.html', context)

def cityDetail(request, slug):
    cityDetail_obj= Location.objects.get(slug = slug)
    context = {
        'cityDetail_obj' : cityDetail_obj
    }
    return render(request, 'city-detail.html', context)


@login_required(login_url='login')       
def bookRoom(request, slug):
    room_obj = Hotel.objects.get(slug = slug)
    hotel_obj = Hotel.objects.all()
    bookform = BookModelForm(instance=room_obj)
    if request.method == 'POST':
        bookform = BookModelForm(request.POST, instance=room_obj)
        if bookform.is_valid():
            fullname = request.POST.get('fullname')
            email = request.POST.get('email')
            guest = request.POST.get('guest')
            check_in = request.POST.get('check_in')
            check_out = request.POST.get('check_out')
            hotel = request.POST.get('hotel')
            booker = request.user
            
            #hotel_id = request.POST.get('hotel')
            #hotel=  Hotel.objects.get(id= hotel_id)
            book = Booking(fullname=fullname, email=email, guest=guest, check_in=check_in,
                            check_out=check_out, booker=booker, hotel=room_obj)
            book.save()
        return redirect('profile')
    else:
        bookform= BookModelForm()
    context = {
        'room_obj': room_obj, 
        'hotel_obj' : hotel_obj,
        'bookform' : bookform
        }
    
    return render(request, 'booking.html', context)
        
        

    
  
        
        
        
      

        
        

    