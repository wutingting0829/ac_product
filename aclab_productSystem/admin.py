from django.contrib import admin

from .models import ProductUser, Product, Book, BookBorrow


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', "name", "content", "photo", "location", "total")
    list_display_links = ('name',)


@admin.register(ProductUser)
class ProductUserAdmin(admin.ModelAdmin):
    list_display = ('id', "user", "key_Product", "created_at", "num")


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author",)


@admin.register(BookBorrow)
class BookBorrowAdmin(admin.ModelAdmin):
    list_display = ("user", "book",)
