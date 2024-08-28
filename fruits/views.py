from django.shortcuts import render, redirect
from django.template import loader
from django.http import JsonResponse
from django.contrib import messages
import datetime
from .models import *
from django.contrib.auth.models import User
import json
from . utils import cookieCart, cartData, guestOrder




#for time
current_date = datetime.datetime.now()

year = current_date.strftime('%Y')

# Create your views here.

def home(request):
    context={'year':year}
    return render (request, 'account/home.html', context)


########### FOR EVERYTHING ON CATEGORIES ##################

def categories(request):
    context={'year':year}
    return render (request, 'categories.html', context)

########### CLOTHINGS ######################
def bags(request):
    data = cartData(request)
    cartItems = data['cartItems']
    bags = Bags.objects.all()
    context={'year':year, 'bags':bags, cartItems:'cartItems'}
    return render (request, 'categories/clothings/bags.html', context)

def blouses(request):
    context={'year':year}
    return render (request, 'categories/clothings/blouses.html', context)

def gele(request):
    context={'year':year}
    return render (request, 'categories/clothings/gele.html', context)

def gowns(request):
    context={'year':year}
    return render (request, 'categories/clothings/gowns.html', context)

def shoes(request):
    context={'year':year}
    return render (request, 'categories/clothings/shoes.html', context)

def tops(request):
    context={'year':year}
    return render (request, 'categories/clothings/tops.html', context)


############### OTHERS ###########################

def jewelries(request):
    context={'year':year}
    return render (request, 'categories/others/jewelries.html', context)

def make_ups(request):
    context={'year':year}
    return render (request, 'categories/others/makeups.html', context)

def purses(request):
    context={'year':year}
    return render (request, 'categories/others/purses.html', context)

def wigs(request):
    context={'year':year}
    return render (request, 'categories/others/wigs.html', context)

def sanitaries(request):
    context={'year':year}
    return render (request, 'categories/others/sanitaries.html', context)

def sunglasses(request):
    context={'year':year}
    return render (request, 'categories/others/sunglasses.html', context)


###########################################

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


def product(request,pk):
    data = cartData(request)
    cartItems = data['cartItems']
    product = Product.objects.get(id=pk)
    context = {'product':product, 'cartItems':cartItems}
    return render(request, 'product.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action'],

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
              
    else:
        customer, order = guestOrder(request, data)
        
        
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

        

    return JsonResponse('payment complete', safe=False)

