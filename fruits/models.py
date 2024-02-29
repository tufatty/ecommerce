from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField("Name", max_length=200, null=True)
    email = models.EmailField("Email",max_length=200)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField("Name:", max_length=200)
    sizes = models.CharField("Sizes:", max_length=300)
    price = models.DecimalField("Price:",max_digits=7, decimal_places=2)
    digital = models.BooleanField(default=False,null=True,blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url  

######### FOR CATEGORIES OF THINGS ##################################################################################################################################
    

    
######### CLOTHINGS ###############    

class Bags(models.Model):
    name = models.CharField("Name:", max_length=200)
    sizes = models.CharField("Sizes:", max_length=300)
    price = models.DecimalField("Price:",max_digits=7, decimal_places=2)
    digital = models.BooleanField(default=False,null=True,blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url  
    

class Blouses(models.Model):
    name = models.CharField("Name:", max_length=200)
    sizes = models.CharField("Sizes:", max_length=300)
    price = models.DecimalField("Price:",max_digits=7, decimal_places=2)
    digital = models.BooleanField(default=False,null=True,blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url  
    


class Gele(models.Model):
    name = models.CharField("Name:", max_length=200)
    sizes = models.CharField("Sizes:", max_length=300)
    price = models.DecimalField("Price:",max_digits=7, decimal_places=2)
    digital = models.BooleanField(default=False,null=True,blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url  
    


class Gowns(models.Model):
    name = models.CharField("Name:", max_length=200)
    sizes = models.CharField("Sizes:", max_length=300)
    price = models.DecimalField("Price:",max_digits=7, decimal_places=2)
    digital = models.BooleanField(default=False,null=True,blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url  
    


class Shoes(models.Model):
    name = models.CharField("Name:", max_length=200)
    sizes = models.CharField("Sizes:", max_length=300)
    price = models.DecimalField("Price:",max_digits=7, decimal_places=2)
    digital = models.BooleanField(default=False,null=True,blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url  
    


class Tops(models.Model):
    name = models.CharField("Name:", max_length=200)
    sizes = models.CharField("Sizes:", max_length=300)
    price = models.DecimalField("Price:",max_digits=7, decimal_places=2)
    digital = models.BooleanField(default=False,null=True,blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url  
    

######### OTHERS ###############    

class Jewelries(models.Model):
    name = models.CharField("Name:", max_length=200)
    sizes = models.CharField("Sizes:", max_length=300)
    price = models.DecimalField("Price:",max_digits=7, decimal_places=2)
    digital = models.BooleanField(default=False,null=True,blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url  
    

class Makeups(models.Model):
    name = models.CharField("Name:", max_length=200)
    sizes = models.CharField("Sizes:", max_length=300)
    price = models.DecimalField("Price:",max_digits=7, decimal_places=2)
    digital = models.BooleanField(default=False,null=True,blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url  
    


class Purses(models.Model):
    name = models.CharField("Name:", max_length=200)
    sizes = models.CharField("Sizes:", max_length=300)
    price = models.DecimalField("Price:",max_digits=7, decimal_places=2)
    digital = models.BooleanField(default=False,null=True,blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url  
    


class Wigs(models.Model):
    name = models.CharField("Name:", max_length=200)
    sizes = models.CharField("Sizes:", max_length=300)
    price = models.DecimalField("Price:",max_digits=7, decimal_places=2)
    digital = models.BooleanField(default=False,null=True,blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url  


class Sunglasses(models.Model):
    name = models.CharField("Name:", max_length=200)
    sizes = models.CharField("Sizes:", max_length=300)
    price = models.DecimalField("Price:",max_digits=7, decimal_places=2)
    digital = models.BooleanField(default=False,null=True,blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url  


######################################################################################################



class Order(models.Model):
    customer =models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField("Date", auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField("Transaction Id", max_length=100, null=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
                
        return shipping      


    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum ([item.quantity for item in orderitems])
        return total
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField("Quantity", default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField("Address", max_length=200, null=False)
    city = models.CharField("City", max_length=200, null=False)
    state = models.CharField("State", max_length=200, null=False)
    zipcode = models.CharField("Zip Code", max_length=200, null=False)
    country = models.CharField("Country", max_length=200, null=False, default='Nigeria')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
   
