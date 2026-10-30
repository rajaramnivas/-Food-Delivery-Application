from django.shortcuts import render,redirect

from .models import Profile,Restaurant,FoodItem,Order

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required


def home(request):
    foods=FoodItem.objects.all()
    return render(request,'home.html',{'foods':foods})

#register
def register(request):
    if(request.method=="POST"):
        user=User.objects.create_user(
            
            username=request.POST['username'],
            password=request.POST['password'],
            
        )
        Profile.objects.create(
            
            user=user,
            role=request.POST['role']
        )
        return redirect('login')
    return render(request,'register.html')


#login
def  userlogin(request):
    if(request.method=="POST"):
            user=authenticate(
                
                username=request.POST['username'],
                password=request.POST['password'],
                
            )
            if(user is not None):
                login(request,user)
                return redirect("home")
    return render(request,"login.html")

#logout
def userlogout(request):
    logout(request)
    return redirect("login")

@login_required
def place_order(request,food_id):
    food=FoodItem.objects.get(id=food_id)
    order1=Order.objects.create(customer=request.user)
    order1.items.add(food)
    
    return redirect("myorders")

@login_required
def my_orders(request):
    orders=Order.objects.filter(customer=request.user)
    return render(request,"myorders.html",{'orders':orders})

@login_required
def delivery_order(request):
    orders=Order.objects.filter(delivery_partner=request.user)
    return render(request,"delivery_orders.html",{'orders':orders})

@login_required
def complete_order(request,order_id):
    o=Order.objects.get(id=order_id)
    o.status="DELIVERD"
    o.save()
    return redirect("delivery_orders")
    
