from django.contrib import admin
from django.urls import path,include
from . import views 


urlpatterns = [
   path('home/',views.home,name='home'),
   path('register/',views.register,name='register'),
   path('login/',views.userlogin,name='login'),
   path('logout/',views.userlogout,name='logout'),
   path('order/<int:food_id>/',views.place_order,name='order'),
   path('myorder/',views.my_orders,name='myorders'),
   path('delivery/',views.delivery_order,name='delivery_orders'),
   path('delivery/complete/<int:order_id>/',views.complete_order,name='completeorder'),
            
      
      
]

   