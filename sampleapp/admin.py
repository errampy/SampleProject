from django.contrib import admin
from sampleapp.models import *
# Register your models here.

class CompanyRegistrationAdmin(admin.ModelAdmin):
    list_display=['company_id','company_name','company_description','established_at','created_at','updated_at']
admin.site.register(CompanyRegistration,CompanyRegistrationAdmin)


class DesignationAdmin(admin.ModelAdmin):
    list_display=['desig_id','desig_name','created_at','updated_at']
admin.site.register(Designation,DesignationAdmin)


class EmployeeRegistrationAdmin(admin.ModelAdmin):
    list_display=['emp_id','emp_name','dob','doj','address','created_at','updated_at']
admin.site.register(EmployeeRegistration,EmployeeRegistrationAdmin)

