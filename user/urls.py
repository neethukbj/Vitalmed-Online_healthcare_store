from django.urls import path
from . import views

urlpatterns = [
    path('',views.home ,name='userhome' ),
    path('signinuser',views.signin,name='signinuser'),
    path('usersignup',views.userSignup,name='usersignup'), 
    path('usersignin',views.userSignin ,name='usersignin'),
    path('otp',views.otplogin ,name='otp'),
    path('otpenter<int:Phone_num>',views.otpenter, name='otpenter'),
    path('phone_number_verification<str:username>',views.phone_number_verification, name='phone_number_verification'),
    path('otpentersignup<int:Phone_num>',views.otpentersignup, name='otpentersignup'),
    path('singnupuser',views.userSignup),
    path('userlogout',views.userlogout,name='userlogout'),
    path('productdisplay<int:id>',views.productDisplay,name='productdisplay') ,
    path('userprofile',views.userprofile,name='userprofile'), 
    path('myorders',views.myorders,name='myorders'), 
    path('ordercancel/<int:id>/',views.ordercancel,name='ordercancel') ,
    path('changepassword',views.changepassword,name='changepassword'),  
    path('search',views.search,name='search'),  
    path('homecart',views.homecart,name='homecart'),  
    path('shopvitamin',views.shopvitamin,name='shopvitamin'),  
    path('shoppersonalcare',views.shoppersonalcare,name='shoppersonalcare'), 
    path('shopmedicine',views.shopmedicine,name='shopmedicine'), 
    path('shopequipment',views.shopequipment,name='shopequipment'), 
    path('limiteddeal',views.limiteddeal,name='limiteddeal'),  
    path('popularcombo',views.popularcombo,name='popularcombo'),  
    
    
    path('addressdelete/<int:id>/',views.addressdelete,name='addressdelete') ,
    path('editaddress/<int:id>/',views.editaddress,name='editaddress') ,



    
    path('orderdetails/<int:id>/',views.orderdetails,name='orderdetails'),
    path('orderreturn/<int:id>/',views.orderreturn,name='orderreturn')  
 

 




    
    




]