from django.db import models
from warehouse.models import Warehouse

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        unique_together = ('product', 'warehouse')

    def __str__(self):
        return f"{self.product.name} in {self.warehouse.name}: {self.quantity}"
    
    def order_point(self):
        pass