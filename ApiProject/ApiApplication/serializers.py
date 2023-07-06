from rest_framework import serializers
from .models import *
class SirketSerializer(serializers.Serializer):
    sirket_id= serializers.IntegerField(label="enter sirket id")
    sirket_isim = serializers.CharField(label="enter sirket isim")
    sirket_adres = serializers.CharField(label="enter sirket adres")
    sirket_tel = serializers.CharField(label="enter sirket tel")
    sirket_email = serializers.EmailField(label="enter sirket email")
    sirket_web = serializers.URLField(label="enter sirket web")

class KisiSerializer(serializers.Serializer):
    kisi_id= serializers.IntegerField(label="enter kisi id")
    kisi_adsoyad = serializers.CharField(label="enter kisi adsoyad")
    kisi_tel = serializers.CharField(label="enter kisi tel")
    kisi_email = serializers.EmailField(label="enter kisi email")
    kisi_sirket = serializers.IntegerField(label="Şirket ID")   
