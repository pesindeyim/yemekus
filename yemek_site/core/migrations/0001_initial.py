# Generated by Django 5.0.7 on 2024-08-18 21:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='YemekKart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=200)),
                ('resim', models.ImageField(upload_to='kart_resimleri/')),
                ('aciklama', models.TextField()),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.kategori')),
            ],
        ),
    ]
