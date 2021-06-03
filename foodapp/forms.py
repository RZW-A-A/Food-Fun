from foodapp.models import Food, Customer, ContactUs, Reservation
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'mobile', 'address', 'proficpic']

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'


class Menusearchform(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['foodname']
