from rest_framework import serializers
from sampleapp.models import *


# Model Based Serializer Defining below
#
class CompanyRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyRegistration
        fields = '__all__' # here will list all the fields whatever is there in models class

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = ['desig_id','desig_name'] # this means will display only specified fields from the models

class EmployeeRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeRegistration
        exclude = ('address',) # this means except specified will display


# here defining normal Serializer that without models so in this case we can define our own fiels that might be or not related to models fields
#For Example
        
class EmployeeDetailsForm(serializers.Serializer):
    name = serializers.CharField(max_length=250)
    father_name = serializers.CharField(max_length=250)
    mother_name = serializers.CharField(max_length=250)
    phone_number = serializers.IntegerField()
    email = serializers.EmailField()
    address = serializers.CharField(max_length=250)

