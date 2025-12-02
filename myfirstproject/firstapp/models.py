
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, null=True, blank=True)
    role = models.CharField(max_length=20, choices=[
        ('Admin', 'Admin'),
        ('PGOwner', 'PGOwner'),
        ('Tenant', 'Tenant'),
    ], default='Tenant')

    def __str__(self):
        return self.user.username
