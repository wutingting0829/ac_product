from django.contrib import admin

# Register your models here.
from .models import ProductUser,Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id',"name" ,"content","photo","location","total")

admin.site.register(Product,ProductAdmin)


class ProductUserAdmin(admin.ModelAdmin):
    list_display = ('id',"user" ,"key_Product","created_at","num")


admin.site.register(ProductUser,ProductUserAdmin)