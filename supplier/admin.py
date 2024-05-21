from django.contrib import admin
from .models import Supplier, PhoneNumber

# Register your models here.
class PhoneNumberInline(admin.StackedInline):
    model = PhoneNumber
    extra = 1


class SupplierAdmin(admin.ModelAdmin):
    inlines = [PhoneNumberInline]


admin.site.register(Supplier, SupplierAdmin)