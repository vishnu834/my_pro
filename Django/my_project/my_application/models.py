from django.db import models
# Create your models here.
class Info(models.Model):
    Name=models.CharField(max_length=30,default="")
    Age=models.CharField(max_length=30,default="")
    DateOfBirth=models.CharField(max_length=30,default="")
    PhoneNumber=models.CharField(max_length=30,default="")
    Address=models.CharField(max_length=30,default="")
    Mail=models.EmailField(max_length=30,default="")

    