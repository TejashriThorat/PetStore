from django.db import models
from django.utils.html  import mark_safe

# Create your models here.
class CustomManager(models.Manager):
    def get_price_range(self,r1,r2):
        return self.filter(price__range = (r1,r2))
    def catlist(self):
        return self.filter(category__exact = "Cat")
    def doglist(self):
        return self.filter(category__exact = "Dog")
    
class Pet(models.Model):
    pet_id = models.IntegerField(primary_key = True)
    pet_name = models.CharField(max_length = 50)
    type = (("Cat","Cat"),("Dog","Dog"))
    category = models.CharField(max_length = 100,choices = type)
    desc =models.CharField(max_length = 255)
    price = models.IntegerField()
    image = models.ImageField(upload_to='pics')

    prod = CustomManager() #object of Custom Manager
    objects = models.Manager() #default manager


    def proImage(self):
        return mark_safe(f"<img src='{self.image.url}' width = '300px' >")
    
class CartItem(models.Model):
    pets = models.ForeignKey(Pet,on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 0)
    date_added = models.DateTimeField(auto_now_add = True)



