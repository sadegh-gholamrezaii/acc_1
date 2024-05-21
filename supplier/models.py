from django.db import models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام تامین کننده")
    address = models.TextField(verbose_name="آدرس")
    website = models.URLField(blank=True, null=True, verbose_name="وبسایت")
    created = models.DateTimeField(auto_now_add=True, verbose_name="زمان ساخته شدن")
    updated = models.DateTimeField(auto_now=True, verbose_name="زمان بروزرسانی")

    class Meta:
        verbose_name = "تامین کننده"
        verbose_name_plural = "تامین کننده ها"

    def __str__(self):
        return self.name
    

class PhoneNumber(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name="تامین کننده")
    phone_number = models.DecimalField(max_digits=11, decimal_places=0, verbose_name="شماره تلفن")

    def __str__(self):
        return self.phone_number