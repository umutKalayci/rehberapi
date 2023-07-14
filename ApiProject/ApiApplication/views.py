from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins
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
  
class SirketApiDetailView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = SirketSerializer
    queryset = Sirket.objects.all()
    lookup_field = 'sirket_id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class KisiApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    serializer_class = KisiSerializer
    queryset = Kisi.objects.all()
    lookup_field = 'kisi_id'

    def get(self, request, kisi_id=None):
        if kisi_id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

class KisiApiDetailView(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = KisiSerializer
    queryset = Kisi.objects.all()
    lookup_field = 'kisi_id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class KisiCagriView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Cagri.objects.all()
    serializer_class = CagriKisiSerializer

    def get(self, request, kisi_id, format=None):
        self.queryset = self.filter_queryset(self.get_queryset())
        self.queryset = self.queryset.filter(arayan_kisi=kisi_id) | self.queryset.filter(aranan_kisi=kisi_id)
        return self.list(request)

class CagriApiView(generics.ListCreateAPIView):
    queryset = Cagri.objects.all()
    serializer_class = CagriSerializer
    
class CagriUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cagri.objects.all()
    serializer_class = CagriSerializer
    lookup_field = 'cagri_id'