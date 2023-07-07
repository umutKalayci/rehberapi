from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


class SirketApiView(APIView):
    serializer_class=SirketSerializer
    def get(self, request, sirket_id=None):
        if sirket_id is not None:
            sirket = Sirket.objects.filter(sirket_id=sirket_id).values()
            if sirket:
                return Response({"Message": f"Şirket ID'si {sirket_id} olan şirket", "Şirket": sirket})
            else:
                return Response({"Message": f"Şirket ID'si {sirket_id} olan şirket bulunamadı"})
        else:
            sirketler = Sirket.objects.all().values()
            return Response({sirketler})
    
    def post(self,request):
        
        print('Request data is:',request.data)
        serializer_obj=SirketSerializer(data=request.data)
        if(serializer_obj.is_valid()):
            sirket = serializer_obj.save()
            sirket_data = serializer_obj.data
            return Response({"Message": "Yeni sirket eklendi!", "Sirket": sirket_data})

        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

class SirketApiPutView(APIView):
    serializer_class=SirketSerializer
    def get(self, request, sirket_id=None):
        if sirket_id is not None:
            sirket = Sirket.objects.filter(sirket_id=sirket_id).values()
            if sirket:
                return Response({"Message": f"Şirket ID'si {sirket_id} olan şirket", "Şirket": sirket})
            else:
                return Response({"Message": f"Şirket ID'si {sirket_id} olan şirket bulunamadı"})
        else:
            sirketler = Sirket.objects.all().values()
            return Response({sirketler})
        
    def put(self, request, sirket_id):
        try:
            sirket = Sirket.objects.get(pk=sirket_id)
            serializer_obj = SirketSerializer(sirket, data=request.data)
            if serializer_obj.is_valid():
                serializer_obj.save()
                return Response({"Message": "Şirket güncellendi!", "Sirket": serializer_obj.data})
            return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
        except Sirket.DoesNotExist:
            return Response({"Message": f"Şirket ID'si {sirket_id} olan şirket bulunamadı"}, status=status.HTTP_404_NOT_FOUND)
    def delete(self, request, sirket_id):
        try:
            sirket = Sirket.objects.get(sirket_id=sirket_id)
            sirket.delete()
            return Response({"Message": f"Şirket ID'si {sirket_id} olan şirket silindi!"})
        except Kisi.DoesNotExist:
            return Response({"Message": f"Şirket ID'si {sirket_id} olan şirket bulunamadı"}, status=status.HTTP_404_NOT_FOUND)


class KisiApiView(APIView):
    serializer_class=KisiSerializer
    def get(self, request, kisi_id=None):
        if kisi_id is not None:
            kisi = Kisi.objects.filter(kisi_id=kisi_id).values()
            if kisi:
                return Response({"Message": f"Kişi ID'si {kisi_id} olan kişi", "Kisi": kisi})
            else:
                return Response({"Message": f"Kişi ID'si {kisi_id} olan kişi bulunamadı"})
        else:
            kisiler = Kisi.objects.all().values()
            return Response({kisiler})
    def post(self,request):
        #sirket = Sirket.objects.get(sirket_id=request.data["sirket_id"])

        print('Request data is:',request.data)
        serializer_obj=KisiSerializer(data=request.data)
        if(serializer_obj.is_valid()):
                kisi = serializer_obj.save()
                kisi_data = serializer_obj.data
                return Response({"Kisi": kisi_data})

        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class KisiApiPutView(APIView):
    serializer_class=KisiSerializer
    def get(self, request, kisi_id=None):
        if kisi_id is not None:
            kisi = Kisi.objects.filter(kisi_id=kisi_id).values()
            if kisi:
                return Response({"Message": f"Kişi ID'si {kisi_id} olan kişi", "Kisi": kisi})
            else:
                return Response({"Message": f"Kişi ID'si {kisi_id} olan kişi bulunamadı"})
        else:
            kisiler = Kisi.objects.all().values()
            return Response({kisiler})
    def put(self, request, kisi_id):
        try:
            kisi = Kisi.objects.get(pk=kisi_id)
            serializer_obj = KisiSerializer(kisi, data=request.data)
            if serializer_obj.is_valid():
                serializer_obj.save()
                return Response({"Message": "Kişi güncellendi!", "Kisi": serializer_obj.data})
            return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
        except Kisi.DoesNotExist:
            return Response({"Message": f"Kişi ID'si {kisi_id} olan kişi bulunamadı"}, status=status.HTTP_404_NOT_FOUND)
        
    
    def delete(self, request, kisi_id):
        try:
            kisi = Kisi.objects.get(kisi_id=kisi_id)
            kisi.delete()
            return Response({"Message": f"Kişi ID'si {kisi_id} olan kişi silindi!"})
        except Kisi.DoesNotExist:
            return Response({"Message": f"Kişi ID'si {kisi_id} olan kişi bulunamadı"}, status=status.HTTP_404_NOT_FOUND)


class CagriApiView(APIView):
    serializer_class = CagriSerializer

    def get(self, request):
        cagrilar = Cagri.objects.all()
        serializer = self.serializer_class(cagrilar, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        arayan_kisi_id = request.data.get("arayan_kisi")
        aranan_kisi_id = request.data.get("aranan_kisi")

        if arayan_kisi_id == 1:
            request.data["cagri_turu"] = "Giden arama"
        elif aranan_kisi_id == 1:
            request.data["cagri_turu"] = "Gelen arama"

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    
class CagriDeleteView(APIView):
    serializer_class = CagriSerializer

    def get(self, request, cagri_id=None):
        if cagri_id is not None:
            cagri = Cagri.objects.filter(cagri_id=cagri_id).values()
            if cagri:
                return Response({"Message": f"Çağrı ID'si {cagri_id} olan çağrı", "Çağrı": cagri})
            else:
                return Response({"Message": f"Çağrı ID'si {cagri_id} olan çağrı bulunamadı"})
        else:
            cagrilar = Cagri.objects.all().values()
            return Response({cagrilar})
    
    def delete(self, request, cagri_id):
        try:
            cagri = Cagri.objects.get(cagri_id=cagri_id)
            cagri.delete()
            return Response({"Message": f"Çağrı ID'si {cagri_id} olan çağrı silindi!"})
        except Cagri.DoesNotExist:
            return Response({"Message": f"Çağrı ID'si {cagri_id} olan çağrı bulunamadı"}, status=status.HTTP_404_NOT_FOUND)