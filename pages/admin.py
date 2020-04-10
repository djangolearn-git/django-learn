from django.contrib import admin
from .models import *

class CustomStudent(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'std', 'batch_number','dateofbirth','division','date_created')
    search_fields = ['first_name','last_name', 'std','batch_number','division','date_created']
    list_display_links = ['first_name']
    list_filter = ['std', 'batch_number','division','date_created']

admin.site.register(Appsettings)
admin.site.register(Student,CustomStudent)


