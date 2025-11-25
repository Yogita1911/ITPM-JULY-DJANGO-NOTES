from django.db import models

class Emp_Details(models.Model):
    Name = models.CharField(max_length=50)
    Address = models.TextField(max_length=100)
    Salary = models.IntegerField()
    Depart_Name = models.CharField(max_length=50)
    join_Date = models.DateField()

    
