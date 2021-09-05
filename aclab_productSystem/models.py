from django.db import models
from django.conf import settings


# Create your models here.

class Product(models.Model):
    name = models.CharField(verbose_name="財產名稱", max_length=100)  # verbose_name="財產名稱"---改系統內建名稱
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='Img/productImg')
    location = models.CharField(max_length=100)
    total = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    key_Product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, verbose_name="借用者財產", related_name="getProduct")
    created_at = models.DateTimeField(auto_now_add=True)
    num = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='Img/bookImg')

    def __str__(self):
        return self.title


class BookBorrow(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, verbose_name="借用書籍", related_name="getBook")
    created_at = models.DateTimeField(auto_now_add=True)
    return_day = models.DateTimeField(verbose_name="歸還日期")

    def __str__(self):
        return f'{self.user} {self.book}'
