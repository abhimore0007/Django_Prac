from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Watch(models.Model):

    name = models.CharField(max_length=100)
    small_description=models.CharField(max_length=300)
    description=models.TextField()
    original_price = models.IntegerField()
    discounted_price = models.IntegerField()
    Watch_image =models.ImageField(upload_to='Watch_image')

    def __str__(self):
        return str(self.name)
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Watch, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
    @property
    def price_and_quantity_total(self):
        return self.product.discounted_price*self.quantity