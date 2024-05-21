from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام مشتری")
    address = models.TextField(blank=True, null=True, verbose_name="آدرس")
    birth_date = models.DateField(blank=True, null=True, verbose_name="تاریخ تولد")
    created = models.DateTimeField(auto_now_add=True, verbose_name="زمان ساخته شدن")
    updated = models.DateTimeField(auto_add=True, verbose_name="زمان بروزرسانی")
    
    class Meta:
        verbose_name = "مشتری"
        verbose_name_plural = "مشتری ها"

    def __str__(self):
        return self.name


class PhoneNumber(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="مشتری")
    phone_number = models.DecimalField(max_digits=11, decimal_places=0, verbose_name="شماره تلفن")

    def __str__(self):
        return self.phone_number