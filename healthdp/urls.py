from django.urls import path
from django.views import View

from healthdp import views
from healthdp.views import (ParenttListview,NotificationcreateView,GuildlinesView,Notificationlists,NotificationUpdateView,
Guildlinelists,GuildlineUpdateView,VaccinationCreate,VaccinationList,VaccinationUpdate,NotificationDeleteView,GuildLineDeleteView,
VaccinationDeleteView,ashaworkerCreate,ashaworkerList,ashaworkerUpdate,ashaworkerDeleteview)
from public.views import informationList

urlpatterns=[
    path('healtdb',informationList.as_view(),name='health-dash'),
    path('healtdb',informationList.as_view(),name='infolist'),
    path('parentlist',ParenttListview.as_view(),name='plist'),
    path('notify',NotificationcreateView.as_view(),name="Notify"),
    path('notificationlist',Notificationlists.as_view(),name='notylist'),
    path('notifications/<int:pk>/update/', NotificationUpdateView.as_view(), name='notification-update'),
    path('notify/<int:pk>/delete',NotificationDeleteView.as_view(),name='noty-delete'),
    path('guildline',GuildlinesView.as_view(),name='guild'),
    path('guildlinelist',Guildlinelists.as_view(),name='guildlist'),
    path('guildline/<int:pk>/delete',GuildLineDeleteView.as_view(),name='guild-delete'),
    path('guildline/<int:pk>/update/', GuildlineUpdateView.as_view(), name='guildline-update'),
    path('vaccinecreate', VaccinationCreate.as_view(), name='vaccine-create'),
    path('vaccinationlist',VaccinationList.as_view(),name='vaccinelist'),
    path('vaccination/<int:pk>/update/', VaccinationUpdate.as_view(), name='vaccine-update'),
    path('vaccin/<int:pk>/delete',VaccinationDeleteView.as_view(),name='vaccine-delete'),
    path('ashaworker',ashaworkerCreate.as_view(),name='ashaworker-create'),
    path('ashaworklist',ashaworkerList.as_view(),name='ashaworker-list'),
    path('ashaworkerupdate/<int:pk>/update',ashaworkerUpdate.as_view(),name='ashaworker-update'),
    path('ashaworker/<int:pk>/delete',ashaworkerDeleteview.as_view(),name='ashaworker-delete')




   
]