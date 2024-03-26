from django.db import models
import datetime
from django.urls import reverse                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
# Create your models here.
cat = (
    ("Top","Top"),
    ("Crop Top","Crop Top"),
    ("Crop Shirt","Crop Shirt"),
    ("Shirt","Shirt"),
    ("Tshirt","Tshirt"),
    ("Crop Tshirt","Crop Tshirt"),
    ("Tank","Tank"),
    ("Chiffon Top","Chiffon Top"),
    ("Dress","Dress"),
    ("Sweater","Sweater"),
    ("Cardigan","Cardigan"),
    ("Hoodie","Hoodie"),
    ("SweatShirt","SweatShirt"),
    ("Pre Winter","Pre Winter"),
    ("Denim Jacket","Denim Jacket"),
    ("Puffer Jacket","Puffer Jacket"),
    ("Trench Coat","Trench Coat"),
    ("Hoodie","Hoodie"),
    ("Shacket","Shacket"),
    ("Jeans","Jeans"),
    ("Trouser","Trouser"),
    ("Cargo","Cargo"),
    ("Shorts","Shorts"),
    ("Skirt","Skirt")
)
typeofstock = (
    ("Special","Special"),
    ("Sale","Sale"),
    ("Drop","Drop"),
    ("General","General")
)


class Products(models.Model):
    ProductName = models.CharField(max_length=255)
    Catgories = models.CharField(max_length=255,choices=cat)
    Price = models.IntegerField()
    TypeOfStock = models.CharField(choices=typeofstock,max_length=255)
    BustOrWaist = models.CharField(max_length=255)
    Condition = models.IntegerField()
    Details = models.TextField()
    Image1 = models.ImageField(upload_to="media/pics", blank=True)
    Image2 = models.ImageField(upload_to="media/pics",blank=True)
    Image3 = models.ImageField(upload_to="media/pics",blank=True)
    Image4 = models.ImageField(upload_to="media/pics",blank=True)
    Image5 = models.ImageField(upload_to="media/pics",blank=True)
    FreeSize = models.IntegerField(default=0)
    Size22 = models.IntegerField(default=0)
    Size23 = models.IntegerField(default=0)
    Size24 = models.IntegerField(default=0)
    Size25 = models.IntegerField(default=0)
    Size26 = models.IntegerField(default=0)
    Size27 = models.IntegerField(default=0)
    Size28 = models.IntegerField(default=0)
    Size29 = models.IntegerField(default=0)
    Size30 = models.IntegerField(default=0)
    Size31 = models.IntegerField(default=0)
    Size32 = models.IntegerField(default=0)
    Size33 = models.IntegerField(default=0)
    Size34 = models.IntegerField(default=0)
    Size35 = models.IntegerField(default=0)
    Size36 = models.IntegerField(default=0)
    Size37 = models.IntegerField(default=0)
    Size38 = models.IntegerField(default=0)
    Size39 = models.IntegerField(default=0)
    Size40 = models.IntegerField(default=0)
    Size41 = models.IntegerField(default=0)
    Size42 = models.IntegerField(default=0)

class Admin_Details(models.Model):
    AdminName = models.CharField(max_length=255)
    AdminEmail = models.CharField(max_length=255)
    AdminPassword = models.CharField(max_length=255)

class Admin_Drop_Link(models.Model):
    DropName = models.CharField(max_length=255)
    DropNum = models.IntegerField(default=0)
    DateTime = models.DateField(default=datetime.date.today())
    DropDate = models.CharField(max_length=255)

class User(models.Model):
    FullName = models.CharField(max_length=255)
    MobileNo = models.IntegerField()
    Emailid = models.EmailField()
    Password = models.CharField(max_length=255)
    ConfirmPassword = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    productsize = models.CharField(null=False, blank=False,max_length=255)
    quantity = models.IntegerField(null=False, blank=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.product}"

    def get_absolute_url(self):
        return reverse("cart:cart_detail")
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    fname = models.CharField(max_length = 255)
    lname = models.CharField(max_length = 255)    
    address = models.TextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length = 255)
    zipcode = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 255)
    # size = models.CharField(max_length = 255, null=False)
    totalprice = models.FloatField()
    # payment_mode = models.CharField(max_length=255)
    payment_id = models.CharField(max_length=255,null=True)
    orderstatus = (
        ('Pending','Pending'),
        ('Out for shipping','Out for shipping'),
        ('Completed','Completed'),
    )
    status = models.CharField(max_length =255,choices = orderstatus, default='Pending')
    message = models.TextField(null=True)
    trackingno = models.CharField(max_length=255, null = True)
    trackinglink = models.CharField(max_length=255,null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.trackingno)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    product = models.ForeignKey(Products, on_delete = models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()
    size = models.CharField(max_length=255)
    
    def __str__(self):
        return '{} - {}'.format(self.order.id, self.order.trackingno)
    
class Billing(models.Model):
    fname = models.CharField(max_length = 255)
    lname = models.CharField(max_length = 255) 
    address = models.TextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length = 255)
    zipcode = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 255)