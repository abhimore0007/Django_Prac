from django.db import models

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