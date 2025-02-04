
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from . models import Parent,information


class UserForm(UserCreationForm):
    class Meta:
        models=User
        fields=('username','email','password','password','coform_password')

    widgets={
        'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
        'email' : forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}),
        'password' :forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}),
        'coform_password' :forms.PasswordInput(attrs={'class':'form-control','placeholder':'confirm'})

    }


class Loginform(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'font-control','placeholder':'username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'font-control','placeholder':'password'}))



class ParentCreateform(forms.ModelForm):
    class Meta:
        model=Parent
        exclude=['payment_date']
        fields = [
            'name', 
            'address', 
            'email', 
            'phone', 
            'gender', 
            'childname', 
            'age', 
            'childgender', 
            'vaccinated',
            'payment',
            'payment_Mode',
            
        ]
        
    widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
            'address': forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}),
            'gender': forms.Select(attrs={'class':'form-control','placeholder':'Gender'}),
            'childname': forms.TextInput(attrs={'class':'form-control','placeholder':'Child Name'}),
            'age': forms.TextInput(attrs={'class':'form-control','placeholder':'Age'}),
            'childgender': forms.Select(attrs={'class':'form-control','placeholder':'Child Gender'}),
            'payment': forms.NumberInput(attrs={'class':'form-control','placeholder':'Payment'}),
            'payment_Mode': forms.Select(attrs={'class':'form-control','placeholder':'Paymentmode'}),
            
    
    }




class informationForms(forms.ModelForm):
    class Meta:
        model=information
        fields = [
            'name',
            'comments',
            'email'
        ]

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'comments':forms.Textarea(attrs={'class':'form-control','placeholder':'comments'}),
           
        }