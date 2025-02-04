from django.shortcuts import render,redirect
from django.core.mail import send_mail

from django.views.generic import View,ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

from healthdp.forms  import NotificationForm,GuildlineForm,VaccinationForm,AshaworkerForm
from  public .models import Parent,information
from healthdp.models import Notification,guildlines,Vaccination,Ashaworkers

# Create your views here.

# class Healtdpdash(View):
    # def get(self,request,*args,**kwags):
    #     return render(request,'healtdpdash.html')
    
class informationList(ListView):
    model = information
    template_name='healtdpdash.html'
    context_object_name='info'  

    def get_queryset(self):
        qs=information.objects.all()
        return qs



class ParenttListview(ListView):
    model=Parent
    template_name='Adminindex.html'
    context_object_name='parent'

    def get_queryset(self):
        qs=Parent.objects.all()
        return qs

    


class NotificationcreateView(CreateView):
    model=Notification
    form_class=NotificationForm
    template_name='notification.html'
    success_url=reverse_lazy('notylist')



class Notificationlists(ListView):
    model=Notification
    template_name='notificationlist.html'
    context_object_name='data'

    def get_queryset(self):
        qs=Notification.objects.all()
        return qs
    


class NotificationDeleteView(View):
    def get(self, request, *args, **kwargs):
        id=kwargs.get('pk')
        Notification.objects.get(id=id).delete()
        return redirect('notylist')



    

class NotificationUpdateView(UpdateView):
    model = Notification
    form_class = NotificationForm
    template_name = 'notification.html'
    success_url = reverse_lazy('notylist') 




class GuildlinesView(CreateView):
    model=guildlines
    form_class=GuildlineForm
    template_name='guildline.html'
    success_url=reverse_lazy('guild')





class Guildlinelists(ListView):
    model=guildlines
    template_name='guildlinelist.html'
    context_object_name='data'

    def get_queryset(self):
        qs=guildlines.objects.all()
        return qs



class GuildLineDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        guildlines.objects.get(id=id).delete()
        return redirect('guildlist')



class GuildlineUpdateView(UpdateView):
    model = guildlines
    form_class = GuildlineForm
    template_name = 'guildline.html'
    success_url = reverse_lazy('guildlist') 




class VaccinationCreate(CreateView):
    model = Vaccination
    form_class = VaccinationForm
    template_name = 'vaccinationcreate.html'
    success_url = reverse_lazy('vaccine-create')


    def form_valid(self, form):
        response = super().form_valid(form)



        title = form.cleaned_data.get('title')

        subject=f"Vaccination Name:{title}"
        message=f'Dear Parent Vaccination is added:{title}'
        from_email='jishnuprasadtctc@gmail.com'
        parent=Parent.objects.all()
        recipient_list=[]
        for i in parent:
            recipient_list.append(i.email)

        send_mail(subject,message,from_email,recipient_list,fail_silently=False)
        return response







class VaccinationList(ListView):
    model = Vaccination
    template_name = 'vaccinationlist.html'
    context_object_name='vaccine'
    def get_queryset(self):
        qs=Vaccination.objects.all()
        return qs
    




class VaccinationUpdate(UpdateView):
    model = Vaccination
    template_name='vaccinationcreate.html'
    form_class=VaccinationForm
    success_url=reverse_lazy('vaccinelist')



class VaccinationDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        Vaccination.objects.get(id=id).delete()
        return redirect('vaccinelist')
    



class ashaworkerCreate(CreateView):
    model= Ashaworkers
    form_class= AshaworkerForm
    template_name='ashaworkercreate.html'
    success_url=reverse_lazy('ashaworker-create')


class ashaworkerList(ListView):
    model = Ashaworkers
    template_name='ashaworkerlist.html'
    context_object_name='ashaworker'
    

    def get_queryset(self):
        qs=Ashaworkers.objects.all()
        return qs
    

class ashaworkerUpdate(UpdateView):
    model= Ashaworkers
    template_name='ashaworkercreate.html'
    form_class=AshaworkerForm
    success_url=reverse_lazy('ashaworker-list')


    
class ashaworkerDeleteview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        Ashaworkers.objects.get(id=id).delete()
        return redirect('ashaworker-list')
        
   
       
