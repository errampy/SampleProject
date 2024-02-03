from rest_framework.views import APIView
from apis_app.serializers import *
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class CompanyRegistrationAPIView(APIView):
    def get(self,request,*args,**kwargs):
        records = CompanyRegistration.objects.all()
        serializers = CompanyRegistrationSerializer(records,many=True)
        return Response(data=serializers.data,status=status.HTTP_200_OK)
        
    def post(self,request,*args,**kwargs):
        serializers = CompanyRegistrationSerializer(data=request.data)
        if serializers.is_valid():
            # write more business logic
            serializers.save()
            return Response(data='success',status=status.HTTP_201_OK)
            
        else:
            return Response(data=serializers.errors,status=status.HTTP_404_NOT_FOUND)