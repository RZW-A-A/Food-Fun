from django.db import models
from  django.contrib.auth.models import User
# Create your models here.
STATUS_CHOICES = (('starters', 'STARTERS'), ('maindish', 'MAINDISH'), ('deserts', 'DESERTS'), ('drinks', 'DRINKS'))


class Food(models.Model):
    foodId = models.AutoField(primary_key=True)
    foodname = models.CharField(max_length=50)
    foodcategory = models.CharField(max_length=20, choices=STATUS_CHOICES, default='maindish')
    foodprice = models.FloatField()
    foodimage = models.ImageField(upload_to='media', blank=True, null=True, default='')
    fooddiscription = models.CharField(max_length=200)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    mobile = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    proficpic = models.ImageField(upload_to='profile', blank=True, null=True, default='/static/images/de.png')
    date_created = models.DateField(auto_now_add=True, null=True)



class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum({item.get_total for item in orderitems})
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum({item.quantity for item in orderitems})
        return total

class Orderitem(models.Model):
    food = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.food.foodprice * self.quantity
        return total

class ContactUs(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
    subject = models.CharField(max_length=150)
    message = models.TextField(max_length=300)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
    mobile = models.CharField(max_length=10)
    no_of_people = models.IntegerField(default='5')
    date = models.DateField(default='2020-11-14')


    def __str__(self):
        return self.name