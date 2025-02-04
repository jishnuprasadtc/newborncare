from django.contrib import admin
from healthdp.models import Vaccination,guildlines,Notification
from public.models import information,Parent

# Register your models here.
admin.site.register(Vaccination),
admin.site.register(guildlines),
admin.site.register(Notification),
admin.site.register(information),
admin.site.register(Parent)
