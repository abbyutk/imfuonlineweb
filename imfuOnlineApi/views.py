
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from imfu_online import models
from imfuOnlineApi import serializers
# Create your views here.

@api_view(['GET'])
def AppUser(request,pk):

    try:
        appusr = models.AppUser.objects.get(pk=pk)
    except:
        return Response(status.HTTP_404_NOT_FOUND)
    serializer = serializers.AppUserSerializer(appusr)
    return Response(serializer.data)

@api_view(['GET'],)
def AppuserOtpLogin(request,contect):

    try:
        appUser = models.AppUser.objects.get(contect=int(contect))
    except:
        return Response(status.HTTP_404_NOT_FOUND)
    serializer = serializers.AppUserSerializer(appUser)
    return Response(serializer.data)

@api_view(['POST'],)
def AppUserLogin(request):

    useremail = request.POST.get("email")
    password = request.POST.get("password")
    try:
        appUser = models.AppUser.objects.get(email=useremail)
    except:
        return Response(status.HTTP_404_NOT_FOUND)

    if appUser.password == password:
        serializer = serializers.AppUserSerializer(appUser)
        return Response(serializer.data)
    else:
        return Response(status.HTTP_404_NOT_FOUND)

@api_view(['POST'],)
def AppUserSignup(request):

    if request.method == "POST":
        serializer = serializers.AppUserSerializer(data=request.data)
        serializer.error_messages
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status.HTTP_404_NOT_FOUND)


@api_view(["PUT"])
def AppUserUpdate(request,pk):

    try:
        appUser = models.AppUser.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = serializers.AppUserSerializer(appUser,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def AppUserFirm(request,pk):

    try:
        firm = models.UserFirm.objects.get(userid=pk)
    except:
        return Response(status.HTTP_404_NOT_FOUND)
    serializer = serializers.FirmSerializer(firm)
    return Response(serializer.data)

@api_view(['POST'])
def AppUserAddFirm(request):

    if request.method == "POST":
        serializer = serializers.FirmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def AppUserUpdateFirm(request,pk):

    try:
        Firm = models.UserFirm.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = serializers.FirmSerializer(Firm,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status.HTTP_404_NOT_FOUND)

@api_view(['GET'],)
def ProductList(request):

    try:
        product_list = models.product.objects.all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = serializers.ProductSerializer(product_list,many=True)
        if serializer:
            return Response(serializer.data)
        else:
            return Response(status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def PrdoductSearch(request,keydata):

    try:
        product_list = models.product.objects.filter(key=keydata)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.ProductSerializer(product_list,many=True)
        if serializer:
            return Response(serializer.data)
        else:
            return Response(status.HTTP_404_NOT_FOUND)

@api_view(['GET'],)
def ProductDetail(request,pk):

    try:
        productDetail = models.product.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serilizer = serializers.ProductSerializer(productDetail)
        if serilizer:
            return Response(serilizer.data)
        else:
            return Response(status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def Order(request):

    serializer = serializers.OredrSerializer(data=request.data)
    print(serializer.error_messages)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status.HTTP_404_NOT_FOUND)

@api_view(['POST'],)
def OrderProduct(request):

    if request.method =="POST":
        serializer = serializers.OredrProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status.HTTP_200_OK)
        else:
            return Response(status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def OrderProductList(request,pk):

    try:
        productlist = models.OredProduct.objects.filter(order=pk)
    except:
        return Response(status.HTTP_404_NOT_FOUND)
    serializer = serializers.OredrProductSerializer(productlist,many=True)
    if serializer:
        return Response(serializer.data)
    else:
        return Response(status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def OrderPending(request,pk):

    try:
        productlist = models.Order.objects.exclude(status="Confirm").exclude(status="Shipped").exclude(status="Delivered").filter(userid=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = serializers.OredrSerializer(productlist,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def OrderProcessing(request,pk):

    try:
        productlist = models.Order.objects.exclude(status="Pending").exclude(status="Cancel").exclude(status="Delivered").filter(userid=pk)
    except:
        return Response(status.HTTP_404_NOT_FOUND)
    serializer = serializers.OredrSerializer(productlist,many=True)
    if serializer:
        return Response(serializer.data)
    else:
        return Response(status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def OrderComplete(request,pk):

    try:
        productlist = models.Order.objects.filter(userid=pk).filter(status="Delivered")
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = serializers.OredrSerializer(productlist,many=True)
    if serializer:
        return Response(serializer.data)
    else:
        return Response(status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'],)
def RemoveOrder(request,pk):

    try:
        order = models.Order.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    DeleteConfitm = order.delete()
    if DeleteConfitm:
        return Response(status.HTTP_202_ACCEPTED)
    else:
        return Response(status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def OrderList(request,pk):

    try:
        orderList = models.Order.objects.filter(userid=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = serializers.OredrSerializer(orderList,many=True)
    if serializer:
        return Response(serializer.data)
    else:
        return Response(status.HTTP_404_NOT_FOUND)

@api_view(['POST'],)
def AddCart(request):

    serializer = serializers.CartSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status.HTTP_200_OK)
    else:
        return Response(status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'],)
def RemoveCart(request,pk):

    try:
        Cart = models.Cart.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if Cart.delete():
        return Response(status.HTTP_200_OK)
    else:
        return Response(status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def Cartlist(request,pk):

    try:
        cartlist = models.Cart.objects.filter(userid=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = serializers.CartSerializer(cartlist,many=True)
    if serializer:
        return Response(serializer.data)
    else:
        return Response(status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'],)
def RemoveAllCart(request,pk):

    try:
        RemoveCratList = models.Cart.objects.filter(userid=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    ConfirmDelete = RemoveCratList.delete()
    if ConfirmDelete:
        return Response(status.HTTP_200_OK)
    else:
        return Response(status.HTTP_404_NOT_FOUND)

@api_view(['GET'],)
def ordercart(request,pk):

    try:
        cart = models.Cart.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    firm = models.UserFirm.objects.get(userid=cart.userid)
    product = models.product.objects.get(pk=cart.product)
    cgst = product.mrp/100 * product.cgst
    sgst = product.mrp/100 * product.sgst
    total = product.mrp + cgst + sgst
    neworedr = models.Order(userid=cart.userid,address=firm.address,status="Pending",item=1,total=total)
    neworedr.save()
    newrderproduct = models.OredProduct(order=neworedr.pk,product=product.pk,count=cart.count,total=total)
    newrderproduct.save()
    confirm = cart.delete()
    return Response(status.HTTP_200_OK)

@api_view(['GET'])
def orderallcart(request,pk):

    try:
        appuser = models.AppUser.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    cart = models.Cart.objects.filter(userid=pk)
    completetotal = 0
    if(len(cart)>0):
        neworedr = models.Order(userid=pk, address=appuser.address, status="Pending",)
        neworedr.save()
        for item in cart:
            product = models.product.objects.get(pk=item.product)
            cgst = product.mrp / 100 * product.cgst
            sgst = product.mrp / 100 * product.sgst
            total = product.mrp + cgst + sgst
            newrderproduct = models.OredProduct(order=neworedr.pk, product=product.pk, count=item.count, total=total)
            completetotal += total
            newrderproduct.save()
        neworedr.item = len(cart)
        neworedr.total = completetotal
        neworedr.save()
        cart.delete()
        return Response(status.HTTP_200_OK)
    else:
        return Response(status.HTTP_404_NOT_FOUND)



