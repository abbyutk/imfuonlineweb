from django.contrib import admin
from imfu_online import models
# Register your models here.
admin.site.register(models.product)
admin.site.register(models.category)
admin.site.register(models.sub_category)
admin.site.register(models.brand)
admin.site.register(models.subadmin)
admin.site.register(models.vendor)
admin.site.register(models.deliveryboy)
admin.site.register(models.AppUser)
admin.site.register(models.UserFirm)
admin.site.register(models.Order)
admin.site.register(models.OredProduct)
admin.site.register(models.Cart)
