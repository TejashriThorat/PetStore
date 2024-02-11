from django.contrib import admin
from . models import Pet,CartItem

# Register your models here.
class PetAdmin(admin.ModelAdmin):
    list_display = ["pet_id","pet_name","category","price","image"]

admin.site.register(Pet,PetAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ["pets","quantity","date_added"]
admin.site.register(CartItem,CartAdmin)