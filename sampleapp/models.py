from django.db import models

# Create your models here.

class CompanyRegistration(models.Model):
    company_id = models.CharField(max_length=50,primary_key=True)
    company_name = models.CharField(max_length=250,unique=True)
    company_description = models.TextField()
    established_at = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Designation(models.Model):
    desig_id = models.CharField(max_length=50,primary_key=True)
    desig_name = models.CharField(max_length=200,unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class EmployeeRegistration(models.Model):
    emp_id = models.CharField(max_length=50,primary_key=True)
    emp_name = models.CharField(max_length=250)
    dob = models.DateField()
    doj = models.DateField()
    address = models.TextField(null=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
