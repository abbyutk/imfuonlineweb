from django.urls import path
from imfuOnlineApi import views

app_name = 'imfuOnlineApi'

urlpatterns = [
    path('appuser/<int:pk>/',views.AppUser,name="appuser"),
    path('appuser/otp/<str:contect>/',views.AppuserOtpLogin,name="AppuserOtpLogin"),
    path('appuser/login/',views.AppUserLogin,name="login"),
    path('appuser/signup/',views.AppUserSignup,name="signup"),
    path('appuser/update/<int:pk>/',views.AppUserUpdate,name="userupdate"),
    path('firm/<int:pk>/',views.AppUserFirm,name="appuserfirm"),
    path('firm/add/',views.AppUserAddFirm,name="addfirm"),
    path('firm/update/<int:pk>/',views.AppUserUpdateFirm,name="updatefirm"),
    path('order/pending/<int:pk>/',views.OrderPending,name="oredrpending"),
    path('order/processing/<int:pk>/',views.OrderProcessing,name="oredrprocessing"),
    path('order/completed/<int:pk>/', views.OrderComplete, name="oredrcompleted"),
    path('product/',views.ProductList,name="produt"),
    path('product/search/<str:keydata>/',views.PrdoductSearch,name="productSearch"),
    path('product/detail/<int:pk>/',views.ProductDetail,name="productDetail"),
    path('cart/add/',views.AddCart,name="addcart"),
    path('cart/remove/<int:pk>/',views.RemoveCart,name="removecart"),
    path('cart/list/<int:pk>/',views.Cartlist,name="cart"),
    path('cart/order/<int:pk>/',views.ordercart,name="ordercart"),
    path('cart/remove/all/<int:pk>/',views.RemoveAllCart,name="removeallcart"),
    path('cart/order/all/<int:pk>/',views.orderallcart,name="oredrall"),
]