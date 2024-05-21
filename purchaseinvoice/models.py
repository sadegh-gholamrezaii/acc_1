from django.db import models
from warehouse.models import Warehouse
from product.models import Product
from supplier.models import Supplier


# Create your models here.
class PurchaseInvoice(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='تامین کننده')
    invoice_date = models.DateField(auto_now_add=True, verbose_name='تاریخ')
    
    class Meta:
        verbose_name = 'فاکتور خرید'
        verbose_name_plural = 'فاکتور های خرید'


class InvoiceItem(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, verbose_name='انبار')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='کالا')
    purechase_invoice = models.ForeignKey(PurchaseInvoice, on_delete=models.CASCADE, verbose_name='فاکتور خرید')
    quantity = models.IntegerField(verbose_name='تعداد')
    unit_price = models.DecimalField(max_digits=12, decimal_places=0)
    # total_price = models.DecimalField(max_digits=12, decimal_places=0)