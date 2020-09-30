from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class subadmin(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contect = models.PositiveIntegerField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class vendor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contect = models.PositiveIntegerField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zone = models.CharField(max_length=100)
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class deliveryboy(models.Model):
    type =models.CharField(max_length=150,null=True)
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    phone = models.PositiveIntegerField(null=True)
    state = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100,null=True)
    zone = models.CharField(max_length=100,null=True)
    vendor = models.ForeignKey(vendor,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class category(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class sub_category(models.Model):
    cat = models.ForeignKey(category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class brand(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class product(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None,null=True)
    title = models.CharField(max_length=100,null=True)
    code = models.CharField(max_length=100,null=True)
    name = models.CharField(max_length=100,null=True)
    category = models.CharField(max_length=200,null=True)
    subcategory = models.CharField(max_length=200,null=True)
    batchno = models.PositiveIntegerField(null=True)
    expdate = models.DateField(null=True)
    type = models.CharField(max_length=200,null=True)
    capacity = models.FloatField(null=True)
    brand = models.CharField(max_length=200,null=True)
    quantity = models.PositiveIntegerField(null=True)
    ptr = models.FloatField(null=True,default=0)
    dptr = models.FloatField(null=True,default=0)
    mrp = models.FloatField(null=True,default=0)
    cgst = models.FloatField(null=True,default=0)
    sgst = models.FloatField(null=True,default=0)
    buy = models.PositiveIntegerField(null=True)
    get = models.PositiveIntegerField(null=True)
    composition = models.CharField(max_length=200)
    key = models.CharField(max_length=50)

    def __str__(self):
        return self.code

class AppUser(models.Model):
    name = models.CharField(max_length=100)
    contect = models.PositiveIntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class UserFirm(models.Model):
    userid = models.PositiveIntegerField(null=True)
    name = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=300,null=True)
    pincode = models.PositiveIntegerField(null=True)
    region = models.CharField(max_length=100,null=True)
    druglicenceNo = models.CharField(max_length=100,null=True)
    gstin = models.CharField(max_length=100,null=True)
    druglicence = models.ImageField(upload_to='DrugLicence',blank=True)

    def __str__(self):
        return self.appUser.name

class Order(models.Model):
    userid = models.PositiveIntegerField(null=True)
    date = models.DateField(auto_now=True,null=True)
    address = models.CharField(max_length=300,null=True)
    status = models.CharField(max_length=50,null=True)
    item = models.PositiveIntegerField(default=False,null=True)
    total = models.PositiveIntegerField(null=True)

    def __str__(self):
        return str(self.pk)

class OredProduct(models.Model):
    order = models.PositiveIntegerField(null=True)
    product = models.PositiveIntegerField(null=True)
    count = models.PositiveIntegerField(default=1,null=True)
    total = models.PositiveIntegerField(null=True)

    def __str__(self):
        return str(self.pk)

class Cart(models.Model):
    userid = models.PositiveIntegerField(null=True)
    product = models.PositiveIntegerField(null=True)
    count = models.PositiveIntegerField()
    total = models.FloatField(null=True)


    def __str__(self):
        return  str(str(self.userid))

