from django.contrib import admin
from .models import Customer, PhoneNumber

# Register your models here.
class PhoneNumberInline(admin.StackedInline):
    model = PhoneNumber
    extra = 1
    

class CustomerAdmin(admin.ModelAdmin):
    inlines = [PhoneNumberInline]
    

admin.site.register(Customer, CustomerAdmin)