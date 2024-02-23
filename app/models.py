

from django.db import models

# Create your models here.
class emp(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    mob=models.IntegerField()

class customer(models.Model):
    NO=models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=20)
    cmob=models.IntegerField()

class product(models.Model):
    pname=models.CharField(max_length=20)
    pcost=models.IntegerField()
    cname=models.ForeignKey(customer,on_delete=models.CASCADE)    

