from rest_framework import serializers
from .models import *

class SirketSerializer(serializers.Serializer):
    sirket_id= serializers.IntegerField(read_only=True)
    sirket_isim = serializers.CharField(required=True)
    sirket_adres = serializers.CharField(required=False, allow_null=True, allow_blank = True)
    sirket_tel = serializers.CharField(required=False, allow_null=True, allow_blank = True)
    sirket_email = serializers.EmailField(required=False, allow_null=True, allow_blank = True)
    sirket_web = serializers.URLField(required=False, allow_null=True, allow_blank = True)
    sirket_profil_fotografi = serializers.CharField(required=False, allow_null=True, allow_blank = True)

    class Meta:
        model = Sirket
        fields = ['sirket_id','sirket_isim', 'sirket_adres', 'sirket_tel', 'sirket_email', 'sirket_web','sirket_profil_fotografi']
    
    
    def create(self, validated_data):
        sirket = Sirket.objects.create(**validated_data)
        return sirket
    
    def update(self, instance, validated_data):
        instance.sirket_isim = validated_data.get('sirket_isim', instance.sirket_isim)
        instance.sirket_adres = validated_data.get('sirket_adres', instance.sirket_adres)
        instance.sirket_tel = validated_data.get('sirket_tel', instance.sirket_tel)
        instance.sirket_email = validated_data.get('sirket_email', instance.sirket_email)
        instance.sirket_web = validated_data.get('sirket_web', instance.sirket_web)
        instance.sirket_profik_fotografi = validated_data.get('sirket_profil_fotografi', instance.sirket_profil_fotografi)

        instance.save()
        return instance
    
    def delete(self, instance):
        instance.delete()

#Bütün kişileri listelerken bu Serializer çağrılıyor.    
class KisiSerializer(serializers.ModelSerializer):
    sirketler = serializers.PrimaryKeyRelatedField(many=True, queryset=Sirket.objects.all(), required=False)
    kisi_email = serializers.EmailField(required=False, allow_null = True, allow_blank = True)
    profil_fotografi = serializers.CharField(required=False, allow_null = True, allow_blank = True)
    
    class Meta:
        model = Kisi
        fields = ['kisi_id', 'kisi_adsoyad', 'kisi_tel', 'kisi_email', 'sirketler','profil_fotografi']
    
    
    def create(self, validated_data):
        sirketler = validated_data.pop('sirketler')
        kisi = Kisi.objects.create(**validated_data)
        kisi.sirketler.set(sirketler)
        return kisi
    def update(self, instance, validated_data):
        sirketler = validated_data.pop('sirketler', [])
        instance = super().update(instance, validated_data)
        instance.sirketler.set(sirketler)
        return instance

    
    def delete(self, instance):
        instance.delete()
      
class CagriSerializer(serializers.ModelSerializer):
    cagri_id =  serializers.IntegerField(read_only=True)
    arayan_kisi = serializers.PrimaryKeyRelatedField(queryset=Kisi.objects.all())
    aranan_kisi = serializers.PrimaryKeyRelatedField(queryset=Kisi.objects.all())
    aciklama = serializers.CharField(required=False, allow_null=True, allow_blank = True)
    arama_nedeni = serializers.CharField(required=False, allow_null=True, allow_blank = True)

    class Meta:
        model = Cagri
        fields = ['cagri_id','aranan_kisi', 'arayan_kisi','tarih', 'cagri_suresi', 'aciklama', 'arama_nedeni']

    def create(self, validated_data):
        arayan_kisi_id = validated_data.get("arayan_kisi").kisi_id
        aranan_kisi_id = validated_data.get("aranan_kisi").kisi_id
        
        return Cagri.objects.create(**validated_data)
    
    #yalnızca çağrı süresinde değişiklik yapmalı.
    def update(self, instance, validated_data):
        instance.cagri_suresi = validated_data.get('cagri_suresi', instance.cagri_suresi)
        instance.save()
        return instance
    
    def delete(self, instance):
        instance.delete()

#KisiCagriView'da bu Serializer çağrılıyor.
class CagriKisiSerializer(serializers.ModelSerializer):
    arayan_kisi = serializers.SerializerMethodField()
    aranan_kisi = serializers.SerializerMethodField()
    aciklama = serializers.CharField(required=False, allow_null=True, allow_blank = True)
    arama_nedeni = serializers.CharField(required=False, allow_null=True, allow_blank = True)
    
    class Meta:
        model = Cagri
        fields = ['cagri_id', 'aranan_kisi', 'arayan_kisi', 'tarih', 'cagri_suresi', 'aciklama', 'arama_nedeni']

    def get_arayan_kisi(self, obj):
        if obj.arayan_kisi.kisi_id == self.context['view'].kwargs['kisi_id']:
            return obj.arayan_kisi.kisi_id
        else:
            serializer = KisiSerializer(obj.arayan_kisi)
            return serializer.data

    def get_aranan_kisi(self, obj):
        if obj.aranan_kisi.kisi_id == self.context['view'].kwargs['kisi_id']:
            return obj.aranan_kisi.kisi_id
        else:
            serializer = KisiSerializer(obj.aranan_kisi)
            return serializer.data