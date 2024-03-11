from django.shortcuts import render
import mysql.connector
from django.db import connection
from .models import Products,Admin_Details,Admin_Drop_Link,User,Cart, Order, OrderItem, TrackingDetails
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProductForm, RegisterForm, DropForm, UserRegisterForm,AdminTrackingDetails
from argon2.exceptions import VerifyMismatchError
import datetime
from django.contrib.auth.hashers import make_password, check_password
from django.http.response import JsonResponse,HttpResponse
from django.contrib import messages
from django.db.models import Sum
from dateutil.relativedelta import relativedelta
from django.db.models import Count
import string
import random
from email import message
import email
from django.core.mail import send_mail
from django.conf import settings
# from django.views.decorators.csrf import csrf_protect
# Create your views here.

#other function
def send_text_email(subject, message, receiver_email_list):
    sender_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, sender_email, receiver_email_list)

def last_day_of_month(date):
    return date.replace(day=1) + relativedelta(months=1) - relativedelta(days=1)

def generate_random_password(length=16):
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    random_password = ''
    for i in range(length):
        random_password = random_password  + random.choice(letters)
    return random_password

# Frontend Functions
def home(request):   
    try: 
        name =request.session['name']
    except KeyError:
        table = Products.objects.all()
        return render(request,"index.html",{'table':table})
    table = Products.objects.all()
    return render(request,"index.html",{'table':table,'name':name})

def product(request,productid):
    if not 'userid' in request.session:
        return redirect('login')
    try: 
        name =request.session['name']
    except KeyError:
        pro_id = Products.objects.get(id=productid)
        return render(request,"index.html",{'pro_id':pro_id})
    pro_id = Products.objects.get(id=productid)
    return render(request, "product-page.html",{'pro_id':pro_id,'name':name})

def categories(request):
    if not 'userid' in request.session:
        return redirect('login')

    return render(request, "categories.html")

# @csrf_protect
def placeorder(request):
    if not 'userid' in request.session:
        return redirect('login')

    if request.method == 'POST':
        neworder = Order()
        neworder.user_id = request.session['userid']
        neworder.fname = request.POST.get('firstname')
        neworder.lname = request.POST.get('lastname')
        neworder.address = request.POST.get('address')
        neworder.city = request.POST.get('city')
        neworder.state = request.POST.get('state')
        neworder.country = request.POST.get('country')
        neworder.zipcode = request.POST.get('code')
        neworder.phone = request.POST.get('phone')
        print(neworder.fname)
        #PAYMENT MODE:
        # neworder.payment_mode = request.POST.get('payment_mode')
        neworder.payment_id = request.POST.get('payment_id')

        cart = Cart.objects.filter(user=request.session['userid'])
        cart_total_price = 0
        for item in cart:
            cart_total_price = cart_total_price + item.product.Price * item.quantity

        neworder.totalprice = cart_total_price
        neworder.save()

        neworderitems = Cart.objects.filter(user=request.session['userid'])
        for item in neworderitems:
            OrderItem.objects.create(
                order=neworder,
                product=item.product,
                price=item.product.Price,
                quantity=item.quantity,
                size = item.productsize
            )

            #Decrease the quantity from order stocks:
            # orderproduct = Products.objects.


        Cart.objects.filter(user=request.session['userid']).delete()
        messages.success(request, "Your order is placed!")

    return redirect("home")

def checkout(request):
    if not 'userid' in request.session:
        return redirect('login')
    
    cartitems = Cart.objects.filter(user_id = request.session['userid'])
    total_price = 0
    for item in cartitems:
        total_price = total_price + item.product.Price * item.quantity

    return render(request, 'check-out.html',{'cartitems':cartitems,'total_price': total_price})

def addtocart(request):
    if not 'userid' in request.session:
        return redirect('login')
    
    if request.method == "POST":
        prod_id = int(request.POST.get('product_id'))

        prod_size = request.POST.get('product_size')
        prod_size_quant = Products.objects.values_list(prod_size).filter(id=prod_id)
        prod_size_quant_final_val=prod_size_quant[0][0]
        print(prod_size_quant_final_val)
        # print(prod_size_quant1.get())
        product_check = Products.objects.get(id=prod_id)
        userid = request.session['userid']
        
        # print(userid)
        if(product_check):
            if(Cart.objects.filter(user_id = userid,product_id = prod_id)):
                return JsonResponse({'status': "Product already added!  "})
            else:
                prod_qty = int(request.POST.get('product_qty'))
                if prod_qty < prod_size_quant_final_val:
                    # print("hello")
                    Cart.objects.create(user_id=userid, product_id = prod_id, quantity= prod_qty,productsize=prod_size)
                    return JsonResponse({'status': "Product added successfully!"})
                else:
                      return JsonResponse({'status': "We have less products"})
        else:
            return JsonResponse({'status':"No such a product found!"})

    return redirect("home")

def razorpaycheck(request):
    if not 'userid' in request.session:
        return redirect('login')
    
    cart = Cart.objects.filter(user=request.session['userid'])
    total_price = 0
    for item in cart:
        total_price = total_price + item.product.Price * item.quantity
    return JsonResponse({
        'total_price' : total_price
    })

def cart(request):
    if not 'userid' in request.session:
        return redirect('login')
    name = request.session['name']
    cart = Cart.objects.filter(user_id = request.session['userid'])
    return render(request, 'shopping-cart.html',{'cart':cart , 'name': name})

def dlt_cart_item(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        cartitem = Cart.objects.get(product_id = prod_id, user= request.session['userid'])
        print(cartitem)
        cartitem.delete()
    return render(request,"shopping-cart.html")

def myorders(request):
    if not 'userid' in request.session:
        return redirect('login')
    name = request.session['name']
    orders = Order.objects.filter(user=request.session['userid'])
    trackingdetails = TrackingDetails.objects.values_list()
    # print(trackingdetails)
    return render(request,"user.html",{'orders':orders,'name':name,'trackingdetails':trackingdetails})

def register(request):
    form = UserRegisterForm
    if request.method == "POST":
        encryptedpwd = make_password(request.POST['Password'])
        print(encryptedpwd)
        pwd = request.POST['Password']
        cpwd = request.POST['ConfirmPassword']
        name = request.POST['FullName']
        mono = request.POST['MobileNo']
        email = request.POST['Emailid']
        # dp = check_password(request.POST['Password'],encryptedpwd)
        # print(dp)
        countmail = User.objects.filter(Emailid=email).count()
        if countmail < 1: 
            print(encryptedpwd)
            form = UserRegisterForm(request.POST or None)
            if form.is_valid():
                if pwd == cpwd:
                    print("hii")
                    data = User(FullName=name,MobileNo=mono,Emailid=email,Password=encryptedpwd,ConfirmPassword=encryptedpwd)
                    data.save()
                # form.save()
                    return redirect("login")
                else:
                    return render(request, 'user-register.html',{'form':form,"message":"Confirm Password must be same to the Password"})
        else:
             return render(request, 'user-register.html',{'form':form,"message2":"Email is already registered"})
    return render(request, 'user-register.html',{'form':form})

def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        user_given_password = request.POST['password']
        _password = User.objects.only("Password").get(Emailid = email).Password
        print(user_given_password)
        matching = check_password(user_given_password,_password)
        # print(matching)
        if matching is True:
            # print("hii")
            id = User.objects.only('id').get(Emailid=email).id
            fullname = User.objects.only('FullName').get(Emailid=email).FullName
            request.session['userid'] = id
            request.session['name'] = fullname
            return redirect("home")
        else:
            return render(request,"login.html")
    return render(request,"login.html")

def forgot_password(request):
    if request.method == 'POST':
        txtemail = request.POST['email']
        count = User.objects.filter(Emailid=txtemail).count()
        if count == 0:
            return render(request,"forgot_password.html",{'message':"Email is not registerd with us!"})
        else:
            new_password = generate_random_password(7)

            user = User.objects.get(Emailid=txtemail)
            user.Password = make_password(new_password)
            user.save()

            subject = "Congratulations, We have recovered your Account!"
            message = f"Your new password is {new_password}"
            recipient_list = [txtemail]
            send_text_email(subject,message,recipient_list)
            return redirect("change_password")
    return render(request,"forgot_password.html")
        
def change_password(request):
    if request.method == "POST":
        txtemail = request.POST['email']
        current_password = request.POST['currentpassword']
        new_password = request.POST['password']
        count = User.objects.filter(Emailid = txtemail).count()
        if count == 0:
            return render(request,"change_password.html",{"message":"Database do not contain this password."})
        else:
            new_password = make_password(new_password)
            user = User.objects.get(Emailid=txtemail)
            user.Password = new_password
            user.ConfirmPassword = new_password
            user.save()
            return redirect('login')
    return render(request,'change_password.html')

def userlogout(request):
    if not 'userid' in request.session:
        return redirect('login')
    name = request.session['name']
    del request.session['userid']
    del request.session['name']
    return render(request, 'user-logout.html',{'message':"logout successully",'name':name})

def logout_page(request):
    if not 'userid' in request.session:
        return redirect('login')

    return render(request,'user-logout.html')



#Backend Functions

def adminregister(request):
    form = RegisterForm
    if request.method == "POST":
        # print("HII")
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            # print("hii")
            form.save()
            return redirect("adminlogin")
    return render(request,'backend-signup.html',{'form':form})

def adminlogin(request):
    if request.method == "POST":
        email = request.POST['email']
        user_given_password = request.POST["password"]
        count = Admin_Details.objects.filter(AdminEmail=email).count()
        if count == 1:
            _password = Admin_Details.objects.only("AdminPassword").get(AdminEmail=email).AdminPassword
            try:
                if _password == user_given_password:
                    id = Admin_Details.objects.only("id").get(AdminEmail=email).id
                    request.session["uid"] = id 
                    return redirect("adminhome")
            except VerifyMismatchError:
                return render(request,"backend-login.html",{"message" : "Invalid email or password"})
        else:
             return render(request,"backend-login.html",{"message" : "Already Registered"})
    else:
        if not 'message' in request.session:
            return render(request, 'backend-login.html')
        else:
            message = request.session["message"]
            del request.session["message"]
    return render(request,"backend-login.html",{"message":"Invalid email or password"})

def logout(request):
    if not 'uid' in request.session:
        return redirect('login')

    del request.session['uid']
    return render(request, 'admin-logout.html',{'message':"logout successully"})

def adminhome(request):
    if not 'uid' in request.session:
        return render(request,"backend-login.html")
    
    dt = datetime.date.today()
    mt = dt.month
    limit = 5
    # orderdetails = Order.objects.all()
    orderitem = OrderItem.objects.all().order_by("-id")[:limit]
    usercount = User.objects.filter(created_at__month=mt).count()
    revenue = Order.objects.all().filter(created_at__month=mt)
    totalorder = Order.objects.filter(created_at__month=mt).count()
    total_rev = 0
    total_revenue = sum(revenue.values_list('totalprice',flat=True)) #5586
    cartitems = Cart.objects.filter(created_at__month=mt).count()

    #for cities

    city_orders = Order.objects.values('city').annotate(order_count=Count('id')).order_by('-order_count').filter(created_at__month=mt)

    # Get the city with the most orders
    if city_orders:
        most_orders_city = city_orders[0]['city']
        most_orders_count = city_orders[0]['order_count']
    else:
        most_orders_city = None
        most_orders_count = 0
    return render(request,"backend-index.html",{'orderitem':orderitem,'usercount':usercount,'total_revenue':total_revenue,'total_order':totalorder,'cartitems':cartitems,'most_orders_city': most_orders_city, 'most_orders_count': most_orders_count})

def adminproduct(request):
    if not 'uid' in request.session:
        return render(request,"backend-login.html")
    table = Products.objects.all()
    return render(request,"backend-products.html",{"table":table})

def adminquantitysize(request):
    if not 'uid' in request.session:
        return render(request,"backend-login.html")
    table = Products.objects.all()
    return render(request,"backend-sizequantity.html",{"table":table})

def insertproduct(request):
    if not 'uid' in request.session:
        return render(request,"backend-login.html")
    form = ProductForm
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        # print("hii")
        if form.is_valid():
            print("hii")
            form.save()
            return redirect("adminproduct") 
    # print("hii")
    # print(form.errors.as_data())
    return render(request,"backend-insert-product.html",{'prod_form':form})
        # with connection.cursor() as cursor:
        #     cursor.execute("insert into NithClothingApp_products (ProductName,Catgories,BustOrWaist,Condition,Image1,FreeSize,Size22,Size23,Size24,Size25,Size26,Size27,Size28,Size29,Size30,Size31,Size32,Size33,Size34,Size35,Size36,Size37,Size38,Size39,Size40,Size41,Size42) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", [productname,categories,bustorwaist,condition,img1,freesize,size22,size23,size24,size25,size26,size27,size28,size29,size30,size31,size32,size33,size34,size35,size36,size37,size38,size39,size40,size41,size42])
        #     cursor.close()
    #     prod.save()
    #     return render(request,'backend-insert-product.html')
    # return render(request,'backend-insert-product.html')

def editproduct(request,productid):
    if not 'uid' in request.session:
        return render(request,"backend-login.html")
    SingleProduct = get_object_or_404(Products,id=productid)
    productform = ProductForm(request.POST or None,request.FILES or None, instance=SingleProduct)
    print("hii")
    if productform.is_valid():
        productform.save()
        return redirect("adminproduct")
    else:
        return render(request,"backend-edit-product.html",{'productform':productform})

def deleteproduct(request,productid):
    if not 'uid' in request.session:
        return render(request,"admin-login.html")
    table = Products.objects.get(id=productid)
    table.delete()
    return redirect("adminproduct")

def adminorder(request):
    orderitem = OrderItem.objects.all().order_by("-id")
    return render(request,"adminorder.html",{'orderitem':orderitem})


def updatetrackingdetails(request,orderid):
    tracking_form = AdminTrackingDetails
    orders = Order.objects.all()
    return render(request,"update-tracking-details.html",{'orders':orders})

def insertadmindrop(request):
    drop_form = DropForm
    if request.method == "POST":
        form = DropForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("adminhome")
    return render(request,"drop-link.html",{"drop_form":drop_form})

def admindrop(request):
    if not 'uid' in request.session:
        return render(request,"backend-login.html")
    table = Admin_Drop_Link.objects.all()
    return render(request,"admin-drop2.html",{"table":table})


def editdrop(request,dropid):
    if not 'uid' in request.session:
        return render(request,"backend-login.html")
    SingleDrop = get_object_or_404(Admin_Drop_Link,id=dropid)
    dropform = DropForm(request.POST or None, instance=SingleDrop)
    print("hii")
    if dropform.is_valid():
        dropform.save()
        return redirect("admindrop")
    else:
        return render(request,"edit-drop.html",{'dropform':dropform})

def deletedrop(request,dropid):
    if not 'uid' in request.session:
        return render(request,"admin-login.html")
    table = Admin_Drop_Link.objects.get(id=dropid)
    table.delete()
    return redirect("admindrop")

def dropproducts(request,dropnum,dropname):
    drop_num = Admin_Drop_Link.objects.get(DropNum=dropnum)
    drop_name = Admin_Drop_Link.objects.get(DropName=dropname)
    products = Products.objects.all()
    todaysdate = datetime.date.today()
    return render(request, "drop-products.html",{'drop_num':drop_num,'drop_name':drop_name,'products':products})

def orderitems(request):
    orderitems = OrderItem.objects.all()
    return render(request,"backend-orderitems.html",{'orderitems':orderitems})