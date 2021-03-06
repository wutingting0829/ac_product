"""ac_product URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name=""),
    path('login', views.Login, name="login"),
    path('borrow', views.borrow, name="borrow"),
    path('return', views.return_products, name="return"),
    path('return/<deleteid>', views.return_delete, name="return_delete"),
    path('logout', views.logout, name="logout"),
    path('all_book', views.all_books, name="all_book"),
    path('borrowbook', views.borrowbook, name="borrowbook"),
    path('returnbook', views.return_book, name="returnbook"),
]
