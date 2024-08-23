from django.urls import path
from . import views
from .views import search_results
urlpatterns = [
    path('search/', search_results, name='search_results'),
    path('', views.ana_sayfa, name='ana_sayfa'),
    path('ana-yemekler/', views.ana_yemekler, name='ana_yemekler'),
    path('sicak-corbalar/', views.sicak_corbalar, name='sicak_corbalar'),
    path('geleneksel-yemekler/', views.geleneksel_yemekler, name='geleneksel_yemekler'),
    path('deniz-urunleri/', views.deniz_urunleri, name='deniz_urunleri'),
    path('ozel-gunmenu/', views.ozel_gun_menu, name='ozel_gun_menu'),
    path('vejetaryen/', views.vejetaryen, name='vejetaryen'),
    path('fast-food/', views.fast_food, name='fast_food'),
    path('cocuk-menu/', views.cocuk_menu, name='cocuk_menu'),
    path('tatlilar/', views.tatlilar, name='tatlilar'),
    path('atistirmaliklar/', views.atistirmaliklar, name='atistirmaliklar'),
    path('saglikli-secenekler/', views.saglikli_secenekler, name='saglikli_secenekler'),
    path('icecekler/', views.icecekler, name='icecekler'),
]
