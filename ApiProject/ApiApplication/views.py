from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from .models import *
from .serializers import *


class SirketApiView(generics.GenericAPIView, mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin):
    serializer_class=SirketSerializer
    queryset= Sirket.objects.all()
    lookup_field = 'sirket_id'

    def get(self, request, sirket_id=None):
        if sirket_id:
            return self.retrieve(request)
        else:
            return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
    
    """
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
    """
  
class SirketApiDetailView(generics.GenericAPIView,mixins.ListModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class=SirketSerializer
    queryset= Sirket.objects.all()
    lookup_field = 'sirket_id'
    def get(self, request, sirket_id=None):
        if sirket_id:
            return self.retrieve(request)
        else:
            return self.list(request)
        
    def put(self, request, sirket_id):
        return self.update(request,sirket_id)
    
    def delete(self, request, sirket_id):
        return self.destroy(request,sirket_id)

class KisiApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    queryset = Kisi.objects.all()
    lookup_field = 'kisi_id'

    def get_serializer_class(self):
        
            return KisiListSerializer

    def get(self, request, kisi_id=None):
        
        if kisi_id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

class KisiApiDetailView(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    queryset = Kisi.objects.all()
    lookup_field = 'kisi_id'

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return KisiDetailUpdateSerializer
        return KisiDetailGetSerializer

    def get(self, request, kisi_id):
        return self.retrieve(request)

    def put(self, request, kisi_id):
        return self.update(request, kisi_id)

    def delete(self, request, kisi_id):
        return self.destroy(request, kisi_id)

class KisiCagriView(APIView):
    def get(self, request, kisi_id, format=None):
        cagrilar = Cagri.objects.filter(arayan_kisi=kisi_id) | Cagri.objects.filter(aranan_kisi=kisi_id)
        serializer = CagriKisiSerializer(cagrilar, many=True, context={'view': self})
        return Response(serializer.data)

class CagriApiView(generics.GenericAPIView, mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin):

    serializer_class = CagriSerializer
    queryset= Cagri.objects.all()
    lookup_field = 'cagri_id'

    def get(self, request, cagri_id=None):
        if cagri_id:
            return self.retrieve(request)
        else:
            return self.list(request)
    def post(self,request):
        return self.create(request)
    
    """
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
    """
    
class CagriDeleteView(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class = CagriSerializer
    queryset= Cagri.objects.all()
    lookup_field = 'cagri_id'

    def get(self, request, cagri_id=None):
        if cagri_id:
            return self.retrieve(request)
        else:
            return self.list(request)
    
    def delete(self, request, cagri_id):
        return self.destroy(request,cagri_id)