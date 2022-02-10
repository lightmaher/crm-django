from django.shortcuts import render
from django.test import tag

from shop.models import Customer, Order, Product, Tag

# Create your views here.
def Dashboard(reqest):

   customers = Customer.objects.all()
   orders = Order.objects.all()
   
   context = {'customers' : customers , 'orders' : orders}
   return render(reqest , 'dashboard.html' , context)

def customer(reqest,id):
    customer = Customer.objects.get(id = id)
    orders = customer.order_set.all()
    context = {'customer' : customer , 'orders' : orders}
    return render(reqest, 'customer.html' , context)
