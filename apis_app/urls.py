from django.urls import path
from apis_app.views import *
urlpatterns = [
    path('company-registration/',CompanyRegistrationAPIView.as_view(),name='company_registration'),
]
