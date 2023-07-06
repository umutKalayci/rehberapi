from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


class SirketApiView(APIView):
    serializer_class=SirketSerializer
    def get(self,request):
        sirketler=Sirket.objects.all().values()
        return Response({"Message":"Sirketler Listesi","Sirketler Listesi":sirketler})
    
    def post(self,request):
        
        print('Request data is:',request.data)
        serializer_obj=SirketSerializer(data=request.data)
        if(serializer_obj.is_valid()):
            sirket = serializer_obj.save()
            sirket_data = serializer_obj.data
            return Response({"Message": "Yeni sirket eklendi!", "Sirket": sirket_data})

        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
    

class KisiApiView(APIView):
    serializer_class=KisiSerializer
    def get(self,request):
        kisiler=Kisi.objects.all().values()
        return Response({"Message":"Kisiler Listesi","Kisi Listesi":kisiler})
    
    def post(self,request):
        #sirket = Sirket.objects.get(sirket_id=request.data["sirket_id"])

        print('Request data is:',request.data)
        serializer_obj=KisiSerializer(data=request.data)
        if(serializer_obj.is_valid()):
                kisi = serializer_obj.save()
                kisi_data = serializer_obj.data
                return Response({"Message": "Yeni kisi eklendi!", "Kisi": kisi_data})

        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)



