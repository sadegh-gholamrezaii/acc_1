from django.db import models
from warehouse.models import Warehouse
from product.models import Product
from customer.models import Customer


# Create your models here.
class SalesInvoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='مشتری')
    invoice_date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'فاکتور فروش'
        verbose_name_plural = 'فاکتور های فروش'


class InvoiceItem(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, verbose_name='انبار')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='کالا')
    sales_invoice = models.ForeignKey(SalesInvoice, on_delete=models.CASCADE, verbose_name='فاکتور فروش')
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=12, decimal_places=0)
    # total_price = models.DecimalField(max_digits=12, decimal_places=0)