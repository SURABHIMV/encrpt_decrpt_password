from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class c_user(models.Model):
     c_name = models.CharField(max_length=100,null=True)
     c_email = models.CharField(max_length=100,null=True)
     c_image= models.ImageField(upload_to="user_image/", null=True, blank=True)
     c_password=models.CharField(max_length=100,null=True)
     c_encrpted=models.CharField(max_length=200,null=True)
     
