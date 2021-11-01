from django.db import models

# Create your models here.
class shopcart(models.Model):
    itemname = models.CharField(max_length=30)
    price = models.IntegerField()
    itemdescription = models.TextField(max_length=200)
    itemdescriptionmain = models.TextField(max_length=2000)
    img=models.ImageField(upload_to='pics')
    def __str__(self):
        return self.itemname