from django.urls import path
from . import views

urlpatterns = [
    #Frontend
    path('home',views.home,name='home'),
    path('product/<int:productid>',views.product,name='product'),
    path('categories',views.categories,name='categories'),
    path('cart',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    path('placeorder',views.placeorder,name = 'placeorder'),
    path('addtocart',views.addtocart, name="addtocart"),
    path('proceed_to_pay', views.razorpaycheck, name='proceed_to_pay'),
    path('dlt_cart_item',views.dlt_cart_item, name="dlt_cart_item"),
    path('myorders',views.myorders,name="my-orders"),
    # path('orderview/<str:t_no>',views.orderview, name='orderview'),
    path("dropproducts/<int:dropnum>/<str:dropname>",views.dropproducts,name="admindrop"),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('userlogout',views.userlogout,name="userlogout"),
    path('logout_page',views.logout_page,name='user_logout'),

    #Backend
    path('adminhome',views.adminhome,name='adminhome'),
    path('adminproduct',views.adminproduct, name='adminproduct'),
    path('insertproduct',views.insertproduct, name='insertproduct'),
    path('adminquantitysize',views.adminquantitysize,name='adminquantitysize'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('adminregister',views.adminregister,name='adminregister'),
    path('editproduct/<int:productid>',views.editproduct,name='editproduct'),
    path('deleteproduct/<int:productid>',views.deleteproduct,name='deleteproduct'),
    path('adminorder',views.adminorder,name='adminorder'),
    path('updatetrackingdetails/<int:orderid>',views.updatetrackingdetails,name='updatetrackingdetails'),
    path('logout',views.logout,name="logout"),
    path('insertadmindrop',views.insertadmindrop,name='insertadmindrop'),
    path("admindrop",views.admindrop,name="admindrop"),
    path('editdrop/<int:dropid>',views.editdrop,name='editdrop'),
    path('deletedrop/<int:dropid>',views.deletedrop,name='deletedrop'),
]