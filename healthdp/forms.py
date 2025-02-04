from django import forms
from django.contrib.auth.models import User

from healthdp .models import Notification,guildlines,Vaccination,Ashaworkers


class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        
        fields=[

            
            'title',
            'description'
            

            


        ]
        widegets={
            
            'title':forms.TextInput(attrs={'class':'form-control','Placeholder':'Title'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Description'})
        }



class GuildlineForm(forms.ModelForm):
    class Meta:
        model=guildlines
        fields=[
            'title',
            'description',
            

        ]

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Description'})
        }



class VaccinationForm(forms.ModelForm):
    class Meta:
        model=Vaccination
        fields=[
            'title',
            'description',
        ]

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Description'})
        }





class AshaworkerForm(forms.ModelForm):
    class Meta:
        model=Ashaworkers
        fields=[
            'name',
            'number',
            'primary_health_center',
            'area',
            'district',
           
        ]


        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'number':forms.NumberInput(attrs={'class':'form-control','placeholder':'Number'}),
            'primary_health_center':forms.TextInput(attrs={'class':'form-control','placeholder':'Primary Health Center'}),
            'area':forms.TextInput(attrs={'class':'form-control','placeholder':'Area'}),
            'district':forms.TextInput(attrs={'class':'form-control','placeholder':'District'}),
            
            
        }