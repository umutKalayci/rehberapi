from rest_framework import serializers
from .models import *
class SirketSerializer(serializers.Serializer):
    sirket_id= serializers.IntegerField(label="enter sirket id")
    sirket_isim = serializers.CharField(label="enter sirket isim")
    sirket_adres = serializers.CharField(label="enter sirket adres")
    sirket_tel = serializers.CharField(label="enter sirket tel")
    sirket_email = serializers.EmailField(label="enter sirket email")
    sirket_web = serializers.URLField(label="enter sirket web")

    def create(self, validated_data):
        sirket = Sirket.objects.create(**validated_data)
        return sirket
    
    def update(self, instance, validated_data):
        instance.sirket_isim = validated_data.get('sirket_isim', instance.sirket_isim)
        instance.sirket_adres = validated_data.get('sirket_adres', instance.sirket_adres)
        instance.sirket_tel = validated_data.get('sirket_tel', instance.sirket_tel)
        instance.sirket_email = validated_data.get('sirket_email', instance.sirket_email)
        instance.sirket_web = validated_data.get('sirket_web', instance.sirket_web)

        instance.save()
        return instance
    
    def delete(self, instance):
        instance.delete()

class KisiSerializer(serializers.Serializer):
    kisi_id= serializers.IntegerField(label="enter kisi id")
    kisi_adsoyad = serializers.CharField(label="enter kisi adsoyad")
    kisi_tel = serializers.CharField(label="enter kisi tel")
    kisi_email = serializers.EmailField(label="enter kisi email")
    kisi_sirket_id = serializers.PrimaryKeyRelatedField(queryset=Sirket.objects.all(), label="Şirket ID")

    def create(self, validated_data):
        kisi_sirket_id = validated_data.pop('kisi_sirket_id').sirket_id
        kisi = Kisi.objects.create(kisi_sirket_id=kisi_sirket_id, **validated_data)
        return kisi
    
    def update(self, instance, validated_data):
        instance.kisi_adsoyad = validated_data.get('kisi_adsoyad', instance.kisi_adsoyad)
        instance.kisi_tel = validated_data.get('kisi_tel', instance.kisi_tel)
        instance.kisi_email = validated_data.get('kisi_email', instance.kisi_email)
        instance.kisi_sirket_id = validated_data.get('kisi_sirket_id', instance.kisi_sirket_id)
        instance.save()
        return instance
    
    def delete(self, instance):
        instance.delete()


class CagriSerializer(serializers.ModelSerializer):
    arayan_kisi = serializers.PrimaryKeyRelatedField(queryset=Kisi.objects.all())
    aranan_kisi = serializers.PrimaryKeyRelatedField(queryset=Kisi.objects.all())

    class Meta:
        model = Cagri
        fields = ['cagri_id','aranan_kisi','tarih', 'arayan_kisi', 'cagri_suresi', 'aciklama', 'arama_nedeni','cagri_turu']

    def create(self, validated_data):
        arayan_kisi_id = validated_data.get("arayan_kisi").kisi_id
        aranan_kisi_id = validated_data.get("aranan_kisi").kisi_id

        if arayan_kisi_id == 1:
            validated_data["cagri_turu"] = "Giden arama"
        elif aranan_kisi_id == 1:
            validated_data["cagri_turu"] = "Gelen arama"

        return Cagri.objects.create(**validated_data)
    
    def delete(self, instance):
        instance.delete()

