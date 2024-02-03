from django.urls import path
from sampleapp.views import *
urlpatterns = [
    path('company-registration/',company_registration,name='company_registration'),
]
