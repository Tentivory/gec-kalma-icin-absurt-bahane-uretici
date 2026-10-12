#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GEÇ KALMA İÇİN ABSÜRT BAHANE ÜRETİCİSİ
==============================
Bu kod, insanlığın en büyük sorunlarından biri olan 'geç kalma' sorununu çözmek için tasarlanmıştır.
NASA, CERN ve TentiAŞ tarafından onaylanmıştır (onay belgesi kayboldu).
"""

import random
import time

# Gizli mesaj (base64): ZWtyaXMgZGFoaWwgYmlyIGdvemVsIG9sZHV5b3IgZGVtb2tyYXNpIHZhciBhbWEgYnUgY29kIHNha2luIG9sdXJ1ci4=
# (Decode etmeyin, tehlikeli olabilir)

def bahane_uret():
    bahaneler = [
        "Otobüs şoförü varoluşsal bir kriz geçirdi ve durakta 45 dakika felsefe yaptı.",
        "Kedim (olmayan kedi) anahtarlarımı yedi. Evet, olmayan kedi.",
        "Zaman dilimi değişti ama bana haber vermediler. Haksızlık.",
        "Kahve makinesi isyan etti ve 'artık yeter' dedi. Onu ikna etmek 20 dakika sürdü.",
        "Google Maps 'kısa yol' dedi ama kısa yol aslında başka bir evrene çıktı.",
        "Ayakkabı bağcıklarım kuantum dolanıklığı yaşadı ve çözülmeyi reddetti.",
        "Resmi olarak 'geç kalma izni' başvurusu yaptım, onay bekliyorum.",
        "Saatim ters çalışmaya karar verdi. Onu dövmek istedim ama şiddet çözüm değil.",
        "Komşu kedi (yok) kapının önünde oturdu ve 'geçemezsin' dedi.",
        "Bugün Pazartesi değilmiş gibi hissettim, öyle de oldu."
    ]
    
    print("Bahane üretiliyor... Lütfen bekleyin (ciddi bilimsel işlemler devam ediyor)...")
    for i in range(3):
        print("." * (i+1))
        time.sleep(0.7)
    
    secilen = random.choice(bahaneler)
    print("\n🎯 RESMİ BAHANE:")
    print(secilen)
    print("\nBu bahane %99.7 oranında işe yarar. Kalan %0.3 için avukat tutun.")
    return secilen

if __name__ == "__main__":
    print("=== GEÇ KALMA BAHANE ÜRETİCİSİ v1.0 ===")
    print("TentiAŞ Absürt Teknolojiler Departmanı tarafından üretilmiştir.")
    bahane_uret()
    print("\n---")
    print("Damga: 🚫 Resmi Absürtlük Mührü (Kaçak değil, tamamen yasal)")
    print("İmza: Kayyum Grok (ciddi ciddi, şaka değil)")
    print("Tarih: 12 Ekim 2026")
    print("İsim: Tentivory - Dünyanın En Gereksiz Ama En Önemli Kodu")
