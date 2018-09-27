from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    def __str__(self):
        return '{}'.format(self.product_name)
    product_id=models.IntegerField(default=0)
    product_description=models.CharField(max_length=500,default="")
    product_size=models.CharField(max_length=500,default="")
    product_price=models.IntegerField(default=0)
    product_photo=models.ImageField(default=0)
    product_quantity=models.IntegerField(default=0)