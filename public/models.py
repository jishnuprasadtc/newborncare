from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Parent(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=200,null=False)
    address=models.CharField(max_length=200,null=False)
    email=models.EmailField(null=False)
    phone=models.CharField(max_length=200,null=False)
    gender_options=(
       ( "Female",'Female'),
        ('Male','Male')
    )
    gender=models.CharField(max_length=200,null=False,choices=gender_options,default='Male')
    childname=models.CharField(max_length=200,null=False)
    age=models.CharField(max_length=200,null=False)
    child_gender=(
        ("Girl","Girl"),
        ('Boy','Boy')
    )
    childgender=models.CharField(max_length=200,null=False,choices=child_gender,default='Boy')
    vaccin=(
        ('Done','Done'),
         ('Pending','Pending')        #we need to define that its a TUPLE,DIc
    )
    vaccinated=models.CharField(max_length=200,null=True,choices=vaccin,default='Done')
    payment=models.IntegerField(default=100)
    type=(
        ('Cash','Cash'),
        ('Upi','Upi')
        )
    payment_Mode=models.CharField(max_length=200,null=False,choices=type,default='Cash')
    status=(
        ('Done','Done'),
        ('Pending','Pending')
    )
    payment_date=models.DateTimeField(null=True,auto_now_add=True)

    
       





class information(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.EmailField(null=True)
    comments=models.TextField(max_length=250,null=True)
    

