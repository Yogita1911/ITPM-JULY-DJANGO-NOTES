from django.db import models

# Create your models here.
class Products(models.Model):
    Name = models.CharField(max_length=20)
    Descriptions = models.CharField(max_length=200)
    Price = models.IntegerField()
    Product_image = models.ImageField(upload_to='Products/')
                                      
    
    def __str__(self):
       return self.Name 


