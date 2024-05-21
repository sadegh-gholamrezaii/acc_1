from django.db import models

# Create your models here.
class Warehouse(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PhoneNumber(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, verbose_name="انبار")
    phone_number = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True, unique=True, verbose_name="شماره تلفن")

    def __str__(self):
        return self.phone_number