from django.contrib import admin

# Register your models here.
from .models import ProductUser, Product, Book, BookBorrow


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', "name", "content", "photo", "location", "total")
    list_display_links = ('name',)


admin.site.register(Product, ProductAdmin)


class ProductUserAdmin(admin.ModelAdmin):
    list_display = ('id', "user", "key_Product", "created_at", "num")


admin.site.register(ProductUser, ProductUserAdmin)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author",)


@admin.register(BookBorrow)
class BookBorrowAdmin(admin.ModelAdmin):
    list_display = ("user", "book",)
