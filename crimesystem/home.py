from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def ActionHomePageInterface(request):
    return render(request,"Homepage.html")


def ActionContactus(request):
    return render(request,"Contactus.html")


def ActionHelpline(request):
    return render(request,"Helpline.html")