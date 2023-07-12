from django.db import models

class Sirket(models.Model):
    sirket_id= models.AutoField(primary_key=True)
    sirket_isim = models.CharField(max_length=50, null=True, blank=True)
    sirket_adres = models.CharField(max_length=100, null=True, blank=True)
    sirket_tel = models.CharField(max_length=11, null=True, blank=True)
    sirket_email = models.EmailField(null=True, blank=True)
    sirket_web = models.URLField(null=True, blank=True)

class Kisi(models.Model):
    kisi_id= models.AutoField(primary_key=True)
    kisi_adsoyad = models.CharField(max_length=50)
    kisi_tel = models.CharField(max_length=11)
    kisi_email = models.EmailField(null=True, blank=True)
    profil_fotografi = models.ImageField(upload_to='profil_fotograflari/', null=True, blank=True)
    #kisi_sirket = models.ForeignKey('Sirket', null=True, on_delete=models.SET_NULL, related_name='kisiler')
    sirketler = models.ManyToManyField('Sirket', related_name='kisiler')

class Cagri(models.Model):
    cagri_id = models.AutoField(primary_key=True)
    arayan_kisi = models.ForeignKey('Kisi', on_delete=models.CASCADE, related_name='giden_aramalar')
    aranan_kisi = models.ForeignKey('Kisi', on_delete=models.CASCADE, related_name='gelen_aramalar')
    tarih = models.DateTimeField(auto_now_add=True)
    cagri_suresi = models.DurationField()
    aciklama = models.CharField(max_length=100)
    arama_nedeni = models.CharField(max_length=50)
    #cagri_turu = models.CharField(max_length=20, choices=(('gelen', 'Gelen arama'), ('giden', 'Giden arama')),default='belirsiz arama')
