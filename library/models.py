from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.TextField(unique=True,max_length=30,primary_key=True)
    password = models.TextField(max_length=16,null=False,blank=False)

class Books(models.Model):
    username = models.TextField(unique=True,max_length=30,primary_key=True)
    book_name = models.TextField(max_length=64,null=False,blank=False)
    pages_total = models.IntegerField(null=False)
    pages_read = models.IntegerField(null=False,default=0)
