from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .models import Product,MyCart,Order,Address
from django.shortcuts import get_object_or_404
from django.contrib import messages
from.address_form import Address_form


from .forms import SignUpForm

def home(request):
    return render(request, 'home.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def product(request):
    data=Product.objects.all()
    return render(request,'product.html',{'data':data})


def description(request,pk):
    item=Product.objects.get(pk=pk)
    return render(request,'description.html',{'item':item})

@login_required
def chakker(request,pk):
    current_user = request.user
    userId = current_user.id
    obj = Product.objects.get(pk=pk)
    data1 = current_user.mycart.all()
    # data2 = current_user.mycart.get(pk=pk)
    # print(data2.quantity)

    l=[]
    for x in data1:
        l.append(str(x.productId))

    if pk in l:
        for i in data1:
            if (str(i.productId) == pk):
                if(obj.left_quantity > i.quantity):
                    i.quantity = i.quantity + 1
                    i.price=obj.price*i.quantity
                    """obj.left_quantity=obj.left_quantity -1
                    obj.save()"""
                    i.save()

    else:
        MyCart.objects.create(user=current_user, productId=pk, productName=obj.productName, price=obj.price,image=obj.image)


    data = current_user.mycart.all()
    totalprice=0
    for v in data:
        totalprice=totalprice+v.price

    return render(request,'MyCart.html',{'data':data,'cartprice':totalprice})


def delete(request,productId):
    current_user = request.user
    obj = Product.objects.get(pk=productId)
    #data = current_user.mycart.get(productId=productId)
    data=current_user.mycart.all()
    for x in data:
            if (str(x.productId) == productId):
                if (x.quantity > 1):
                    x.quantity = x.quantity - 1
                    x.price = x.price - obj.price
                    x.save()
                else:
                    x.delete()
    return render(request,'MyCart.html', {'data':data})



def Ads(request):
    if request.method == 'POST':
        form = Address_form(request.POST)
        if form.is_valid():
             data=Address.objects.create(
                 user=request.user,
                 first_name=form.cleaned_data.get('first_name'),
                 last_name=form.cleaned_data.get('last_name'),
                 # email=form.cleaned_data.get('email'),
                 current_address=form.cleaned_data.get('address'))
             print(type(data.id))
             return render(request,'order.html',{'data':data})


    else:
        form = Address_form()
        return render(request, 'delivery_address.html', {'form': form})

def order(request,pk):
    pk=int(pk)
    current_user=request.user
    data1 = current_user.mycart.all()
    datta = current_user.address.get(pk=pk)
    print(datta.first_name)
    for x in data1:
        Order.objects.create(user=current_user,productName=x.productName,total_price=x.price,quantity=x.quantity,address = datta,image = x.image)
        obj = Product.objects.get(id=x.productId)
        obj.left_quantity = obj.left_quantity - x.quantity
        obj.save()
    data1.delete()
    data2=current_user.order.all()
    return render(request,'orderdetails.html',{'data':data2})











