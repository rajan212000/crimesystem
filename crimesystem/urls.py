"""crimesystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import AdminCtrl
from . import UserCtrl,UserRegCtrl,ComplaintCtrl,home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/',home.ActionHomePageInterface),
    path('contactus/',home.ActionContactus),
    path('helpline/',home.ActionHelpline),
    path('adminlogin/', AdminCtrl.AdminLogin),
    path('checkadminlogin', AdminCtrl.checkAdminLogin),
    path('userlogin/', UserCtrl.UserLogin),
    path('checkuserlogin', UserCtrl.checkUserLogin),
    path('userinterface/', UserRegCtrl.UserInterface),
    path('userdetailsubmit',UserRegCtrl.userDetailSubmit),
    path('complaintinterface/',ComplaintCtrl.compalintInterface),
    path('usercomplaintsubmit',ComplaintCtrl.userDetailSubmit),
    path('displayall/',AdminCtrl.ActionSearchComplaintspage),
    path('displaythana/',AdminCtrl.ActionComplaintThanaJson),
    path('displaycomplaintjson/',AdminCtrl.ActionDisplayComplaintjson),
    path('adminlogout/',AdminCtrl.Actionadminlogout),
    path('userlogout/',UserCtrl.Actionuserlogout),
    path('userdisplayall/',UserCtrl.ActionDisplayAllComplaint),
    path('admindisplayall/',AdminCtrl.Actiondisplayall),
    path('editstatus/',AdminCtrl.ActionEditStatus),
    path('savestatus/',AdminCtrl.ActionSaveStatus),
    path('viewcomplaintuser/',UserCtrl.ActionViewComplaintUser),
    path('userprofile/',UserCtrl.ActionUserProfile),
    path('usersaveprofile',UserCtrl.ActionUserSaveProfile),
    path('usersavepic',UserCtrl.ActionUserSavePic),
    path('changepassword/',UserCtrl.ActionChangePassword),
    path('savepassword/',UserCtrl.ActionSavePassword),
]
urlpatterns+=staticfiles_urlpatterns()