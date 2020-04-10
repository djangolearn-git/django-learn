from django.shortcuts import render, HttpResponse
from .models import *
import django.conf as conf
from django.contrib import messages
from django.core.paginator import InvalidPage, Paginator


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
    return render(request, 'pages/index.html')


def Students(request):
    studentdata = Student.objects.all()

    paginator = Paginator(studentdata, 5, orphans=0)

    is_paginated = True if paginator.num_pages > 1 else False
    page = request.GET.get('page') or 1
    try:
       current_page = paginator.page(page)
            # except:
    except InvalidPage as e:
       messages.error(request, str(e))
       current_page = paginator.page(1)

            # context = {
            #     'pending_tasks': pending_tasks,
            # }
    context = {
                    'current_page': current_page,
                    'is_paginated': is_paginated,
                    'paginator': paginator
                }    

    return render(request,'pages/students.html',context)
