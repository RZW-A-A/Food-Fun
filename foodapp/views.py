from django.shortcuts import render, redirect
from foodapp.models import Food, User, Customer, Order, Orderitem, ContactUs, Reservation
from foodapp.forms import FoodForm, Menusearchform, CustomerForm, CreateUserForm, ContactUsForm, ReservationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .utils import cartData, cookieCart
import json
from django.contrib.auth.models import Group
# Create your views here.
def home_view(request):
    return render(request, 'foodapp/home.html')

def aboutus_view(request):
    return render(request, 'foodapp/aboutus.html')

def menu_view(request):
    form = Menusearchform(request.POST or None)
    if request.method == 'POST':
        food = Food.objects.filter(foodname__icontains=form['foodname'].value())
        context = {'food': food, 'form': form}
        return render(request, 'foodapp/menu.html', context)
    else:
        food = Food.objects.all()
    return render(request, 'foodapp/menu.html', {'food': food, 'form': form})

def profile_view(request):
    user = request.user
    customer = Customer.objects.filter(user=user)
    return render(request, 'accounts/profile.html', {'customer': customer})

def reservation_view(request):
    if request.method == 'POST':
        form = ReservationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/reservation')
    else:
        form = ReservationForm()
    return render(request, 'foodapp/reservation.html', {'form': form})

def reservationlist_view(request):
    reserve = Reservation.objects.all()
    return render(request, 'foodapp/reservationlist.html', {'reserve': reserve})

def register_view(request):
    user = request.user
    if request.method == 'POST':
        form = CustomerForm(data=request.POST, files=request.FILES, user=user)
        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form = CustomerForm()
    return render(request, 'accounts/register.html',{'form': form})

def contactus_view(request):
    if request.method == 'POST':
        form = ContactUsForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/contactus')
    else:
        form = ContactUsForm()
    return render(request, 'foodapp/contactus.html', {'form': form})

def contactuslist_view(request):
    contactus = ContactUs.objects.all()
    return render(request, 'foodapp/contactuslist.html', {'contactus': contactus})


def foodlist_view(request):
    food = Food.objects.all()
    return render(request, 'foodapp/food_list.html', {'food': food})

def addfood_view(request):
    if request.method == 'POST':
        food = FoodForm(data=request.POST, files=request.FILES)
        if food.is_valid():
            food.save()
            return redirect('/food_list')
    else:
        food = FoodForm()
    return render(request, 'foodapp/addfood.html', {'food': food})

def deletefood_view(request, foodId):
    food = Food.objects.get(foodId=foodId)
    food.delete()
    return redirect('/food_list')

def updatefood_view(request, foodId):
    food = Food.objects.get(foodId=foodId)
    if request.method == 'POST':
        form = FoodForm(data=request.POST, files=request.FILES, instance=food)
        if form.is_valid():
            form.save()
            return redirect('/food_list')
    form = FoodForm(instance=food)
    return render(request, 'foodapp/updatefood.html', {'form': form})

def customerlist_view(request):
    customer = Customer.objects.all()
    return render(request, 'foodapp/customerlist.html', {'customer': customer})

def updateprofile_view(request):
    context = {}
    customer = Customer.objects.get(user__id=request.user.id)
    context['customer'] = customer
    if request.method == 'POST':
        name = request.POST['name']
        #email = request.POST['email']
        mobile = request.POST['mobile']
        address = request.POST['address']
        #user = User.objects.get(id=request.user.id)
        #user.email = email
        #user.save()
        customer.name = name
        customer.mobile = mobile
        customer.address = address
        customer.save()
        if 'image' in request.FILES:
            img = request.FILES['image']
            customer.proficpic = img
            customer.save()
    return render(request, 'accounts/updateprofile.html', context)

def signup_view(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            messages.info(request, "User is created" + username)
            return redirect('/login')
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        if request.user.customer:
            return redirect('/home')
        else:
            return redirect('register')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/register')
            else:
                messages.info(request, 'Username OR password is incorrect')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('/login')

def cart(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'foodapp/cart.html', context)

def updateItem(request):
    data = json.loads(request.body, encoding='utf-8')
    foodId = data['foodId']
    action = data['action']
    print('Action:', action)
    print('foodId:', foodId)

    customer = request.user.customer
    food = Food.objects.get(foodId=foodId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = Orderitem.objects.get_or_create(order=order, food=food)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def orderlist_view(request):
    data = cartData(request)
    order = data['order']
    orderitem = Orderitem.objects.all()
    return render(request, 'foodapp/orderlist.html', {'orderitem': orderitem, 'order': order})
