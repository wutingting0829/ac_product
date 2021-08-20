from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .models import Product,ProductUser
from django.contrib import auth

#首頁
def Index(request):
    products = Product.objects.all()  # 取出所有財產data
    return render(request, "index.html", locals()) #固定的東西

#使用者登入介面
def Login(request):
    if request.user.is_authenticated:  # 登入會導回index
        return redirect('')
    if request.method == "POST": #進入url的方法
        username = request.POST['studentID'] #透過login.html input的name取得studentID
        password = request.POST['InputPassword'] #透過login.html input的name取得InputPassword
        user = authenticate(username=username, password=password) #驗證使用者
       #判斷user是否存在↑
        if user is not None:
            login(request, user)
            return redirect('')
        else:
            result="error"
    return render(request, "login.html", locals())

#新增借用
def borrow(request):
    if not request.user.is_authenticated:  # 未登入會導回登入畫面
        return redirect('login')

    products = Product.objects.all() #取出所有財產data
    error = ""
    if request.method == "POST":
        borrows = request.POST.getlist('borrowOrNot')
        for i in range(len(borrows)):
            if int(borrows[i]) >0 :
                if int(products[i].total)>int(borrows[i]):
                    ProductUser.objects.create(user=request.user,key_Product = products[i],num = borrows[i])
                    total=str(int(products[i].total)-int(borrows[i])) #算出剩餘數量
                    #更新網頁剩餘數量
                    product_new_account = Product.objects.get(id=products[i].id)
                    product_new_account.total = total
                    product_new_account.save()
                    print(borrows[i],products[i].total)
                else:
                    error += products[i].name+"數量不足喔~~\n"
    return render(request, "borrow.html", locals())


def return_products(request):
    if not request.user.is_authenticated: #未登入會導回登入畫面
        return redirect('login')

    user_products_list = ProductUser.objects.filter(user=request.user)  #取出使用者借用財產項目
    print(user_products_list)


    return render(request, "return.html", locals()) #回傳到前端

def return_delete(request,deleteid):
    print(deleteid)

    userProduct_delete = ProductUser.objects.get(id=deleteid) #得到欄位實體
    total = str(int(userProduct_delete.key_Product.total) + int(userProduct_delete.num))  # 數量加回去
    userProduct_delete.key_Product.total = total #回喘給total
    userProduct_delete.key_Product.save() #存檔
    userProduct_delete.delete()
    return  redirect("return")

def logout(request):
    auth.logout(request)
    return redirect("")


