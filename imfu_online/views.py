import datetime

from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import HttpResponse
from imfu_online import forms
from imfu_online import models
from django.contrib.auth.models import User
from datetime import date
# Create your views here.

def index(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('imfu_online:home')
            else:
                return HttpResponse("user is not active")
        else:
            return HttpResponse("Useraname or Password is wrong !")
    else:
        return render(request,'index.html',context={})

@login_required
def user_logout(request):
    logout(request)
    return redirect("index")

@login_required
def home(request):
    return render(request,'imfu_online/home.html',context={})

@login_required
def product(request):
    product = models.product.objects.all()
    return render(request,'imfu_online/product.html',context={"product":product})

login_required
def yourproduct(request,pk):
    user = User.objects.get(pk=pk)
    product = models.product.objects.filter(user=user)
    return render(request,'imfu_online/yourproduct.html',context={"product":product})

@login_required
def add_product(request,pk):
    form = forms.product_form()
    category = models.category.objects.all()
    subcategory = models.sub_category.objects.all()
    brand = models.brand.objects.all()
    if request.method =="POST":
        user = User.objects.get(pk=pk)
        product = forms.product_form(data=request.POST)
        if product.is_valid():
            product.save()
            return redirect("imfu_online:product")
        else:
            return HttpResponse(product.errors)
    else:
        return render(request,'imfu_online/add_product.html',context={"form":form,"brand":brand,"category":category,"subcategory":subcategory})

@login_required
def update_product(request,pk):
    product = models.product.objects.get(pk=pk)
    category = models.product.objects.all()
    subcategory = models.product.objects.all()
    brand = models.brand.objects.all()

    if request.method == "POST":
        product.titel = request.POST.get("title")
        product.code = request.POST.get("code")
        product.name = request.POST.get("name")
        product.category = request.POST.get("category")
        product.subcategory = request.POST.get("subcategory")
        product.type = request.POST.get("type")
        product.capacity = request.POST.get("capacity")
        product.brand = request.POST.get("brand")
        product.quantity = request.POST.get("quantity")
        product.ptr = request.POST.get("ptr")
        product.mrp = request.POST.get("mrp")
        product.buy = request.POST.get("buy")
        product.get = request.POST.get("get")
        product.composition = request.POST.get("composition")
        product.key = request.POST.get("key")
        product.save()
        return redirect("imfu_online:product")
    else:
        return render(request,'imfu_online/update_product.html',context={"product":product,"category":category,"subcategory":subcategory,"brand":brand})

@login_required
def remove_product(request,pk):
    product = models.product.objects.get(pk=pk)
    product.delete()
    return redirect("imfu_online:product")

@login_required
def brand(request):
    brand = models.brand.objects.all()
    return render(request,'imfu_online/brand.html',context={"brand":brand})

@login_required
def add_brand(request):
    if request.method == "POST":
        brand = request.POST.get("brand")
        new_brand = models.brand(name=brand)
        new_brand.save()
        return redirect("imfu_online:brand")
    else:
        return render(request,'imfu_online/add_brand.html',context={})

@login_required
def remove_brand(request,pk):
    brand = models.brand.objects.get(pk=pk)
    brand.delete()
    return redirect("imfu_online:brand")

def category(request):
    category = models.category.objects.all()
    return render(request,'imfu_online/category.html',context={"category":category})

@login_required
def add_category(request):
    if request.method =="POST":
        category = request.POST.get("category")
        new_category = models.category(name=category)
        new_category.save()
        return redirect("imfu_online:category")
    else:
        return render(request,'imfu_online/add_category.html',context={})

@login_required
def remove_category(request,pk):
    category = models.category.objects.get(pk=pk)
    category.delete()
    return redirect("imfu_online:category")

def subcategory(request):
    subcategory = models.sub_category.objects.all()
    return render(request,'imfu_online/subcategory.html',context={"subcategory":subcategory})

@login_required
def add_subcategory(request):
    form = forms.subcategory_form()
    if request.method == "POST":
        subcategory = forms.subcategory_form(request.POST)
        if subcategory.is_valid():
            subcategory.save()
            return redirect("imfu_online:subcategory")
        else:
            return HttpResponse("form not valid")
    else:
        return render(request,'imfu_online/add_subcategory.html',context={"form":form})

@login_required
def remove_subcategory(request,pk):
    subcategory = models.sub_category.objects.get(pk=pk)
    subcategory.delete()
    return redirect("imfu_online:subcategory")

@login_required
def subadmin(request):
    subadmin = models.subadmin.objects.all()
    return render(request,'imfu_online/subadmin.html',context={'subadmin':subadmin})

@login_required
def add_subadmin(request):
    form = forms.user_form()
    if request.method == "POST":
        contect = request.POST.get("contect")
        state = request.POST.get("state")
        city = request.POST.get("city")
        password = request.POST.get("password")
        user = forms.user_form(request.POST)
        if user.is_valid():
            new_user = user.save(commit=False)
            new_user.is_staff=True
            new_user.set_password(password)
            new_user.save()
            new_subadmin = models.subadmin(user=new_user,contect=contect,state=state,city=city)
            new_subadmin.save()
            return redirect("imfu_online:subadmin")
        else:
            return HttpResponse(user)
    else:
        return render(request,'imfu_online/add_subadmin.html',context={'form':form})

@login_required
def remove_subadmin(request,pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return redirect("imfu_online:subadmin")

def update_subadmin(request,pk):
    subadmin = models.subadmin.objects.get(pk=pk)
    if request.method == "POST":
        update_subadmin = User.objects.get(pk=subadmin.user.pk)
        update_subadmin.username = request.POST.get("username")
        update_subadmin.first_name = request.POST.get("name")
        update_subadmin.email = request.POST.get("email")
        update_subadmin.set_password(request.POST.get("password"))
        update_subadmin.save()
        subadmin.mobile = request.POST.get("contect")
        subadmin.state = request.POST.get("state")
        subadmin.city = request.POST.get("city")
        subadmin.save()
        return redirect("imfu_online:subadmin")
    else:
        return render(request,'imfu_online/update_subadmin.html',context={"subadmin":subadmin})

@login_required
def user(request):
    userdata = models.AppUser.objects.all()
    return render(request,'imfu_online/user.html',context={'users':userdata})

@login_required
def vendor(request):
    vendor = models.vendor.objects.all()
    return render(request,'imfu_online/vendor.html',context={"vendor":vendor})

@login_required
def add_vendor(request):
    form = forms.user_form()
    if request.method == "POST":
        user = forms.user_form(request.POST)
        contect = request.POST.get("contect")
        company = request.POST.get("company")
        state = request.POST.get("state")
        city = request.POST.get("city")
        zone = request.POST.get("zone")
        password = request.POST.get("password")
        print(user.errors)
        if user.is_valid():
            new_user = user.save()
            new_user.set_password(password)
            new_vendor = models.vendor(user=new_user,contect=contect,state=state,city=city,zone=zone,company=company)
            new_vendor.save()
            return redirect("imfu_online:vendor")
        else:
            return HttpResponse("form is not valid !")
    else:
        return render(request,'imfu_online/add_vendor.html',context={"form":form})

@login_required
def remove_vendor(request,pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return redirect("imfu_online:vendor")

@login_required
def update_vendor(request,pk):
    vendor = models.vendor.objects.get(pk=pk)
    if request.method == "POST":
        user = User.objects.get(pk=vendor.user.pk)
        user.username = request.POST.get('username')
        user.first_name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.set_password(request.POST.get('password'))
        vendor.contect = request.POST.get("contect")
        vendor.company = request.POST.get("company")
        vendor.state = request.POST.get("state")
        vendor.city = request.POST.get("city")
        vendor.zone = request.POST.get("zone")
        user.save()
        vendor.save()
        return redirect("imfu_online:vendor")
    else:
        return render(request,'imfu_online/update_vendor.html',context={"vendor":vendor})

@login_required
def order(request):
    orderdata = models.Order.objects.filter(status="Pending")
    return render(request,'imfu_online/order.html',context={"orders":orderdata})

@login_required
def neworder(request):
    orderdata = models.Order.objects.filter(date=date.today())
    return render(request,'imfu_online/neworder.html',context={"orders":orderdata})

@login_required
def allorder(request):
    orderdata = models.Order.objects.all()
    return render(request,'imfu_online/allorder.html',context={"orders":orderdata})

@login_required
def neworder(request):
    orderdata = models.Order.objects.filter(date=date.today())
    return render(request,'imfu_online/neworder.html',context={"orders":orderdata})

@login_required
def deliveryboy(request):
    deliveryboy = models.deliveryboy.objects.all()
    return render(request,'imfu_online/deliveryboy.html',context={"deliveryboy":deliveryboy})

@login_required
def add_deliveryboy(request):
    form = forms.deliveryboy_form()
    vendor = models.vendor.objects.filter(user__is_staff=False)
    if request.method == "POST":
        deliveryboy = forms.deliveryboy_form(request.POST)
        vendor = request.POST.get('vendor')
        if deliveryboy.is_valid():
            new_deliveryboy = deliveryboy.save(commit=False)
            new_deliveryboy.state = request.POST.get('state')
            new_deliveryboy.city = request.POST.get('city')
            new_deliveryboy.zone = request.POST.get('zone')
            new_deliveryboy.type = request.POST.get('type')
            new_deliveryboy.vendor = models.vendor.objects.get(pk=vendor)
            new_deliveryboy.save()
            return redirect("imfu_online:deliveryboy")
        else:
            return HttpResponse("from is not valid")
    else:
        return render(request,'imfu_online/add_deliveryboy.html',context={"form":form,'vendor':vendor})

@login_required
def remove_deliveryboy(request,pk):
    deliveryboy = models.deliveryboy.objects.get(pk=pk)
    deliveryboy.delete()
    return redirect("imfu_online:deliveryboy")

@login_required
def update_deliverboy(request,pk):
    deliveryboy = models.deliveryboy.objects.get(pk=pk)
    vendor = models.vendor.objects.filter(user__is_staff=False)
    if request.method == "POST":
        deliveryboy.name = request.POST.get('name')
        deliveryboy.email = request.POST.get('email')
        deliveryboy.phone = request.POST.get('contect')
        deliveryboy.state = request.POST.get('state')
        deliveryboy.city = request.POST.get('city')
        deliveryboy.zone = request.POST.get('zone')
        print(request.POST.get('type'))
        deliveryboy.type = request.POST.get('type')
        deliveryboy.vendor = models.vendor.objects.get(pk=request.POST.get('vendor'))
        deliveryboy.save()
        return redirect("imfu_online:deliveryboy")
    else:
        return render(request,'imfu_online/update_deliveryboy.html',context={'deliveryboy':deliveryboy,'vendor':vendor})

@login_required
def invoice(request):
    return render(request,'imfu_online/invoice.html',context={})

@login_required
def stock(request):
    return render(request,'imfu_online/stock.html',context={})

@login_required
def report(request):
    return render(request,'imfu_online/report.html',context={})

