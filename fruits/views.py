from django.shortcuts import render, redirect
from django.template import loader
from django.http import JsonResponse
from django.contrib import messages
import datetime
from .models import *
from django.contrib.auth.models import User
import json
from . utils import cookieCart, cartData



#for time
current_date = datetime.datetime.now()

year = current_date.strftime('%Y')

# Create your views here.

def store(request):
    data = cartData(request)
    cartItems = data['cartItems']
    
    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems,}
    return render(request, 'store.html', context)

def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
        

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'cart.html', context)


def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
  

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'checkout.html', context)
    
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
        
    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer = customer,
                order = order,
                address = data['shipping']['address'],
                city = data['shipping']['city'],
                state = data['shipping']['state'],
                zipcode = data['shipping']['zipcode'],
                country = data['shipping']['country'],              

            )

    else:
        print('User is not logged in ...')
    return JsonResponse('payment complete', safe=False)

