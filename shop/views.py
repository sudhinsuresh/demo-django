from django.shortcuts import render
from .models import Category,Products
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
# def home(request):
#     return render(request,'category.html')

def allproductcat(request):
    c=Category.objects.all()
    return render(request,'category.html',{'c':c})

def allproducts(request,p):
    c=Category.objects.get(slug=p)
    p=Products.objects.filter(category__slug=p)
    return render(request,'products.html',{'p':p,'c':c})

def productdetails(request,slug):
    d=Products.objects.get(slug=slug)
    return render(request,'productdeatils.html',{'d':d})



def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
        user.save()

    return render(request, 'signup.html')



def handle_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('pass1')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return allproductcat(request)
        else:
            messages.error(request,"Invalid Credentials")


    return render(request,'login.html')



def handle_logout(request):
    logout(request)
    return handle_login(request)



