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


class Cagri(models.Model):
    cagri_id = models.IntegerField(primary_key=True)
    arayan_kisi = models.ForeignKey('Kisi', on_delete=models.CASCADE, related_name='giden_aramalar')
    aranan_kisi = models.ForeignKey('Kisi', on_delete=models.CASCADE, related_name='gelen_aramalar')
    tarih = models.DateTimeField(auto_now_add=True)
    cagri_suresi = models.DurationField()
    aciklama = models.CharField(max_length=100)
    arama_nedeni = models.CharField(max_length=50)
    cagri_turu = models.CharField(max_length=20, choices=(('gelen', 'Gelen arama'), ('giden', 'Giden arama')),default='belirsiz arama')
