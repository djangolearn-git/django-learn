from django.shortcuts import render,HttpResponse
from .models import Appsettings
import django.conf as conf

def Initappdata():
    # COMPANY NAME
    get_key_name = Appsettings.objects.get(key='COMPANY_NAME')
    conf.settings.COMPANY_NAME = get_key_name.value
    # APP VERSION
    get_key_name = Appsettings.objects.get(key='APP_VERSION')
    conf.settings.APP_VERSION = get_key_name.value

    get_key_name = Appsettings.objects.get(key='DEVELOPER_NAME')
    conf.settings.DEVELOPER_NAME = get_key_name.value

    get_key_name = Appsettings.objects.get(key='SOFTWARE_COMPANY_NAME')
    conf.settings.SOFTWARE_COMPANY_NAME = get_key_name.value
    # COMPANY LONG NAME
    get_key_name = Appsettings.objects.get(key='COMPANY_LONG_NAME')
    conf.settings.COMPANY_LONG_NAME = get_key_name.value
    
    # get_key_name = Appsettings.objects.get(key='')
    # conf.settings. = get_key_name.value

def index(request):
    Initappdata()
    return render(request,'pages/index.html')
