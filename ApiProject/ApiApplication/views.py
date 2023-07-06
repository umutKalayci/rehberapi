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


            Sirket.objects.create(
                            sirket_id=serializer_obj.data.get("sirket_id"),
                            sirket_isim=serializer_obj.data.get("sirket_isim"),
                            sirket_adres=serializer_obj.data.get("sirket_adres"),
                            sirket_tel=serializer_obj.data.get("sirket_tel"),
                            sirket_email=serializer_obj.data.get("sirket_email"),
                            sirket_web=serializer_obj.data.get("sirket_web"),
                            )
        
        sirket=Sirket.objects.all().filter(sirket_id=request.data["sirket_id"]).values()
        return Response({"Message":"Yeni sirket eklendi!","Sirket":sirket})

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
                kisi_id = serializer_obj.data.get("kisi_id")
                kisi_adsoyad = serializer_obj.data.get("kisi_adsoyad")
                kisi_tel = serializer_obj.data.get("kisi_tel")
                kisi_email = serializer_obj.data.get("kisi_email")
                sirket_id = serializer_obj.data.get("sirket_id")

                if "sirket_id" in serializer_obj.data:
                    sirket = Sirket.objects.get(sirket_id=sirket_id)
                    Kisi.objects.create(
                        kisi_id=kisi_id,
                        kisi_adsoyad=kisi_adsoyad,
                        kisi_tel=kisi_tel,
                        kisi_email=kisi_email,
                        sirket=sirket
                    )

                kisi = Kisi.objects.all().filter(kisi_id=kisi_id).values()
                return Response({"Message": "Yeni kisi eklendi!", "Kisi": kisi})
        else:
            return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)



