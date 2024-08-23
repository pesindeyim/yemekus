from django.db import models

class Kategori(models.Model):
    isim = models.CharField(max_length=100)

    def __str__(self):
        return self.isim

class YemekKart(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    isim = models.CharField(max_length=200)
    resim = models.ImageField(upload_to='kart_resimleri/')
    aciklama = models.TextField()

    def __str__(self):
        return self.isim
