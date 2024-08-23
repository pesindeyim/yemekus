from django.contrib import admin
from .models import Kategori, YemekKart

class YemekKartAdmin(admin.ModelAdmin):
    list_display = ['isim', 'kategori']

admin.site.register(Kategori)
admin.site.register(YemekKart, YemekKartAdmin)
