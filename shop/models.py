from django.db import models


# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    product_desc=models.CharField(max_length=50)
    product_category=models.CharField(max_length=50,default="")
    product_subcategory=models.CharField(max_length=50,default="")
    product_date=models.DateField()
    price=models.IntegerField(default=0)
    img=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name