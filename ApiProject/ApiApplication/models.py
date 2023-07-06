from django.db import models

class Sirket(models.Model):
    sirket_id= models.IntegerField(primary_key=True)
    sirket_isim = models.CharField(max_length=50)
    sirket_adres = models.CharField(max_length=100)
    sirket_tel = models.CharField(max_length=11)
    sirket_email = models.EmailField()
    sirket_web = models.URLField()

class Kisi(models.Model):
    kisi_id= models.IntegerField(primary_key=True)
    kisi_adsoyad = models.CharField(max_length=50)
    kisi_tel = models.CharField(max_length=11)
    kisi_email = models.EmailField()
    kisi_sirket = models.ForeignKey('Sirket', null=True, on_delete=models.SET_NULL, related_name='kisiler')
