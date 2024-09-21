from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)  # نام محصول
    description = models.TextField()         # توضیحات محصول
    price = models.DecimalField(max_digits=10, decimal_places=2)  # قیمت
    stock = models.IntegerField()            # تعداد موجودی
    available = models.BooleanField(default=True)  # وضعیت موجودی
    created = models.DateTimeField(auto_now_add=True)  # تاریخ ایجاد
    updated = models.DateTimeField(auto_now=True)      # تاریخ آخرین به‌روزرسانی

    def __str__(self):
        return self.name
