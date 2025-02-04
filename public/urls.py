from django import views
from django.urls import path
from django.views import View
from . import views


from . views import ( RegistraionView,loginview,Dashboard,ParentCreateView,logouts,InfromationslistView,
                     GuildlineView,combined_view,VaccinationListChild,InformationCreate,informationList,Profile,ProfileUpdate,ashaworkerList
)

urlpatterns=[
    path('register/',RegistraionView,name='regs'),
    path('login/',loginview,name='log'),
    path('',Dashboard.as_view(),name='dash'),
    path('parent/add',ParentCreateView.as_view(),name='parentadd'),
    path('profile/',views.Profile.as_view(),name='profile'),
    path('profile/<int:pk>/update',ProfileUpdate.as_view(),name='update-profile'),
    path('logout/',logouts,name='logout'),
    path('information/',combined_view, name='combined_view'),
    path('childvaccine/',VaccinationListChild.as_view(),name='child-vaccine'),
    path('doubts/',InformationCreate.as_view(),name='doubt'),
    path('ashaworkerlisting/',ashaworkerList.as_view(),name='asha-listing')
    

    






]