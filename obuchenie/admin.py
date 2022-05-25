from django.contrib import admin

# Register your models here.
from .models import *

class NG_groupsAdmin(admin.ModelAdmin):
    list_display = ('id', 'ng_client', 'ng_tel', 'ng_predpay', 'ng_pismo')
    list_display_links = ('id', 'ng_client')
    search_fields = ('ng_client', 'ng_email')
    list_editable = ('ng_predpay', 'ng_pismo')

class NG_courseAdmin(admin.ModelAdmin):
    list_display = ('id', 'ng_groupname', 'ng_start')
    list_display_links = ('id', 'ng_groupname', 'ng_start')
    search_fields = ('id', 'ng_groupname', 'ng_start')

admin.site.register(NG_Groups, NG_groupsAdmin)
admin.site.register(NG_course, NG_courseAdmin)