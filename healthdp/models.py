from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserLogins(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    password = models.CharField(max_length=20)


class Notification(models.Model):
    
    title = models.CharField(max_length=200,null=False)
    description = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
       


class guildlines(models.Model):
    
    title = models.CharField(max_length=200,null=False)
    description = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
       





class Vaccination(models.Model):
    
    title = models.CharField(max_length=200,null=False)
    description = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
       


class Ashaworkers(models.Model):
    name= models.CharField(max_length=200,null=True)
    number= models.IntegerField(null=True)
    primary_health_center= models.CharField(max_length=200,null=True)
    area=models.CharField(max_length=200,null=True)
    district=models.CharField(max_length=200,null= True)
    created_at = models.DateTimeField(auto_now_add=True)