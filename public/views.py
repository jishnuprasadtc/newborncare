from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,ListView,UpdateView,DetailView
from django.contrib import messages
from django. contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout 
from django.core.mail import send_mail
from django.conf import settings

from . models import Parent,information
from healthdp .models import Notification,guildlines,Vaccination,UserLogins,Ashaworkers
from . forms import ParentCreateform,informationForms


# Create your views here.


class Dashboard(View):
    def get(self, request):
        return render(request,'dashboad.html')


def RegistraionView(request):
    if request.method=='POST':
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        coform_password=request.POST.get('coform_password') 
        print(password,coform_password,email)
        if coform_password==password:
            user=User.objects.create_user(username=username,email=email,password=password)
            print("user is created")


            UserLogins.objects.create(user=user,password=password)
            
            return redirect('log')
    return render (request,'reg.html')


def loginview(request):
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        print(user)
        if user:
            login(request,user)
            if user.is_staff:
                print(user)
                return redirect('health-dash')
            else:
                return redirect('combined_view')
        
        
    return render(request,'log.html')


def logouts(request):    
    logout(request)
    return redirect('log')





class ParentCreateView(CreateView):
    model = Parent
    form_class=ParentCreateform
    template_name='parentadd.html'
    success_url= reverse_lazy('parentadd')

    def form_valid(self,form):
         data=form.cleaned_data
         if Parent.objects.filter(user=self.request.user, **data).exists():
            messages.warning(self.request, "The details you entered already exist.")
            return redirect('parentadd')
         form.instance.user = self.request.user
         messages.success(self.request, "Parent details added successfully.")
         return super().form_valid(form)






class Profile(ListView):
    model=Parent
    template_name='profile.html'
    context_object_name='profile'


    def get_queryset(self):
       
        qs=Parent.objects.filter(user=self.request.user)
        print(self.request.user)
        print(qs)
        return  qs

class ProfileUpdate(UpdateView):
    model = Parent
    form_class=ParentCreateform
    template_name='parentadd.html'
    success_url=reverse_lazy('combined_view')
 
        
    






class InfromationslistView(ListView):
    model = Notification
    context_object_name='info'
    template_name='information.html'

    def get_queryset(self):
        qs=Notification.objects.all()
        return qs
    

class GuildlineView(ListView):
    model = guildlines
    context_object_name='guild'
    template_name='information.html'

    def get_queryset(self):
        qs=guildlines.objects.all()
        return qs




def combined_view(request):
    info = Notification.objects.all()
    guild = guildlines.objects.all()
    return render(request, 'information.html', {'info': info, 'guild': guild})






class VaccinationListChild(ListView):
    model = Vaccination
    template_name='VaccinationListparent.html'
    context_object_name='vaccination'

    def get_queryset(self):
        qs= Vaccination.objects.all()
        return qs



 
class InformationCreate(CreateView):
    model= information
    form_class=informationForms
    template_name='doubt.html'
    success_url=reverse_lazy('dash')

    def form_valid(self, form):
        responds= super().form_valid(form)

       


        name=form.cleaned_data.get('name')
        comments=form.cleaned_data.get('comments')
        subject=f'I am {name}'
        message=f'{comments}'
        admin_email = settings.EMAIL_HOST_USER
        sender_list=[]  
        public=information.objects.all()
        for i in public:
            sender_list.append(i.email)
        receipt_email=[admin_email]
        
        send_mail(subject, message, admin_email, receipt_email, fail_silently=False)
        return responds

class informationList(ListView):
    model = information
    template_name='healtdpdash.html'
    context_object_name='info'  

    def get_queryset(self):
        qs=information.objects.all()
        return qs





class ashaworkerList(ListView):
    model = Ashaworkers
    template_name='ashaworker_listing.html'
    context_object_name='worker'
    

    def get_queryset(self):
        qs=Ashaworkers.objects.all()
        return qs