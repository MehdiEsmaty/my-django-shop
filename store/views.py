from django.shortcuts import render
from .models import Product  # مدل محصولات را ایمپورت کنید

def home(request):
    products = Product.objects.all()  # تمام محصولات را از پایگاه‌داده دریافت کنید
    return render(request, 'store/home.html', {'products': products})  # محصولات را به قالب ارسال کنید
