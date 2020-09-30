from rest_framework import serializers
from imfu_online import models


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AppUser
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.category
        fields = '__all__'

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.sub_category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.product
        fields = '__all__'

class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserFirm
        fields = '__all__'

class OredrSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'

class OredrProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OredProduct
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = '__all__'