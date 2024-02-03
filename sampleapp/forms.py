from django import forms
from sampleapp.models import *

# Model Based Form Defining below
#
class CompanyRegistrationForm(forms.ModelForm):
    class Meta:
        model = CompanyRegistration
        fields = '__all__' # here will list all the fields whatever is there in models class

class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = ['desig_id','desig_name'] # this means will display only specified fields from the models

class EmployeeRegistrationForm(forms.ModelForm):
    class Meta:
        model = EmployeeRegistration
        exclude = ('address',) # this means except specified will display




# here defining normal form that without models so in this case we can define our own fiels that might be or not related to models fields
#For Example
        
class EmployeeDetailsForm(forms.Form):
    name = forms.CharField(max_length=250)
    father_name = forms.CharField(max_length=250)
    mother_name = forms.CharField(max_length=250)
    phone_number = forms.IntegerField()
    email = forms.EmailField()
    address = forms.CharField(max_length=250)

