from django.shortcuts import render,redirect
from sampleapp.forms import *
# Create your views here.

def company_registration(request):
    if request.method == 'GET':
        form = CompanyRegistrationForm()
        context = {
            'form':form,
        }
        template_name = 'sampleapp/company_registration.html'
        return render(request,template_name,context)
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()# this is respoisble to save data into related table
            return redirect('company_registration')
        else:
            context = {
                'form':form,
            }
            template_name = 'sampleapp/company_registration.html'
            return render(request,template_name,context)

