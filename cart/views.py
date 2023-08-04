from django.shortcuts import render,redirect
from shop.models import Products
from django.contrib.auth.models import User
from cart.models import Cart,Account,Order

# Create your views here.
def cartview(request):
    total=0
    user=request.user
    try:
        cart=Cart.objects.filter(user=user)
        for i in cart:
            total+=i.quantity*i.product.price
            
            
    except Cart.DoesNotExist:
        pass 
    return render(request,'cart.html',{'cart':cart,'total':total})


def add_to_cart(request,p):
    p=Products.objects.get(id=p)
    user =request.user
    try:
        cart=Cart.objects.get(user=user,product=p)
        if(cart.quantity<cart.product.stock):
            cart.quantity+=1
            cart.save()
    except Cart.DoesNotExist:
        cart=Cart.objects.create(user=user,product=p,quantity=1)
        cart.save()

        
            
    return redirect('cart:cartview')


def cart_remove(request,p):
    p=Products.objects.get(id=p)
    user=request.user
    try:
        cart=Cart.objects.get(user=user,product=p)
        if(cart.quantity>1):
            cart.quantity-=1
            cart.save()
        else:
            cart.delete()
    except Cart.DoesNotExist:
        pass
    return redirect('cart:cartview')



def cart_delete(request,p):
    p=Products.objects.get(id=p)
    user = request.user

    try:
        cart = Cart.objects.get(user=user, product=p)
        cart.delete()
    except Cart.DoesNotExist:
        pass

    return redirect('cart:cartview')


def orderform(request):
    total=0
    if request.method =='POST':
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        accountno =request.POST.get('accountno')
        user=request.user
        cart=Cart.objects.filter(user=user)
        for i in cart:
             total +=i.quantity*i.product.price
        ac=Account.objects.get(accountnumber=accountno)
        if ac.amount>=total:
            ac.amount =ac.amount-total
            ac.save()
            for i in cart:
                order =Order.objects.create(user=i.user,product=i.product,address=address,phone=phone,order_status="Paid",no_of_items=i.quantity)
                order.save()
                i.product.stock=i.product.stock-i.quantity
                i.product.save()
            cart.delete()
            msg="Order Placed Successfully"
            return render(request,'orderdetail.html',{'msg':msg})
        else:
            msg="Insufficient Amount. you cannot place order"
            return render(request,'orderdetail.html',{'msg':msg})


    return render(request,'orderform.html')


def order_view(request):
    user=request.user
    order=Order.objects.filter(user=user,order_status="Paid")
    return render(request,'orderview.html',{'order':order,'user':user})