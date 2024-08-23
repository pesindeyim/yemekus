from django.shortcuts import render
from .models import YemekKart, Kategori
def search_results(request):
    query = request.GET.get('q', '')  # Varsayılan olarak boş string al
    results = []
    if query:
        # Sorgu yalnızca belirli uzunluktaki sonuçları filtreler
        results = YemekKart.objects.filter(isim__icontains=query)
    return render(request, 'search_results.html', {'results': results, 'query': query})
def ana_sayfa(request):
    yemek_kartlari = YemekKart.objects.all()
    return render(request, 'ana_sayfa.html',{'yemek_kartlari': yemek_kartlari})

def ana_yemekler(request):
    yemek_kartlari = YemekKart.objects.filter(kategori = Kategori.objects.get(isim="Ana Yemek"))
    return render(request, 'kategori/ana_yemekler.html', {'yemek_kartlari': yemek_kartlari})

def sicak_corbalar(request):
    yemek_kartlari = YemekKart.objects.filter(kategori = Kategori.objects.get(isim="Çorbalar"))
    return render(request, 'kategori/sicak_corbalar.html', {'yemek_kartlari': yemek_kartlari})

def geleneksel_yemekler(request):
    yemek_kartlari = YemekKart.objects.filter(kategori=Kategori.objects.get(isim="Geleneksel Yemekler"))
    return render(request, 'kategori/geleneksel_yemekler.html', {'yemek_kartlari': yemek_kartlari})

def deniz_urunleri(request):
    yemek_kartlari = YemekKart.objects.filter(kategori=Kategori.objects.get(isim="Deniz Ürünleri"))
    return render(request, 'kategori/deniz_urunleri.html', {'yemek_kartlari': yemek_kartlari})

def ozel_gun_menu(request):
    yemek_kartlari = YemekKart.objects.filter(kategori=Kategori.objects.get(isim="Özel Gün Menüleri"))
    return render(request, 'kategori/ozel_gun_menu.html', {'yemek_kartlari': yemek_kartlari})

def vejetaryen(request):
    yemek_kartlari = YemekKart.objects.filter(kategori=Kategori.objects.get(isim="Vejetaryen"))
    return render(request, 'kategori/vejetaryen.html', {'yemek_kartlari': yemek_kartlari})

def fast_food(request):
    yemek_kartlari = YemekKart.objects.filter(kategori=Kategori.objects.get(isim="Fast Food"))
    return render(request, 'kategori/fast_food.html', {'yemek_kartlari': yemek_kartlari})

def cocuk_menu(request):
    yemek_kartlari = YemekKart.objects.filter(kategori=Kategori.objects.get(isim="Çocuk Menüsü"))
    return render(request, 'kategori/cocuk_menu.html', {'yemek_kartlari': yemek_kartlari})

def tatlilar(request):
    yemek_kartlari = YemekKart.objects.filter(kategori=Kategori.objects.get(isim="Tatlılar"))
    return render(request, 'kategori/tatlilar.html', {'yemek_kartlari': yemek_kartlari})

def atistirmaliklar(request):
    yemek_kartlari = YemekKart.objects.filter(kategori=Kategori.objects.get(isim="Atıştırmalıklar"))
    return render(request, 'kategori/atistirmaliklar.html', {'yemek_kartlari': yemek_kartlari})

def saglikli_secenekler(request):
    yemek_kartlari = YemekKart.objects.filter(kategori=Kategori.objects.get(isim="Sağlıklı Seçenekler"))
    return render(request, 'kategori/saglikli_secenekler.html', {'yemek_kartlari': yemek_kartlari})

def icecekler(request):
    yemek_kartlari = YemekKart.objects.filter(kategori=Kategori.objects.get(isim="İçecekler"))
    return render(request, 'kategori/icecekler.html', {'yemek_kartlari': yemek_kartlari})
