# python ile otomatik json içerik oluşturma

import json
from datetime import datetime, timedelta

# Ders listesi - Örnek
dersler = [
    {"title": "Gözlem Birimi", "post": "posts/01-veri-ne-demek.ipynb", "tags": ["gözlem", "veri", "temel kavramlar"]},
    {"title": "Veri Bilimi Nedir?", "post": "posts/02-veri-bilimi-nedir.ipynb", "tags": ["veri bilimi", "tanım", "analiz"]},
    {"title": "İstatistik Nedir?", "post": "posts/03-istatistik-nedir.ipynb", "tags": ["istatistik", "veri bilimi", "karar verme"]},
    {"title": "İstatistik ve Veri Bilimi", "post": "posts/04-istatistik-ve-veri-bilimi.ipynb", "tags": ["veri bilimi", "istatistiksel yöntemler", "modelleme"]}
]

# Basit tarih atama
start_date = datetime(2025, 5, 16)
for i, ders in enumerate(dersler):
    ders["date"] = (start_date + timedelta(days=i)).strftime("%Y-%m-%d")

# JSON olarak yazdır
with open("fcontext.json", "w", encoding="utf-8") as f:
    json.dump({
        "site_title": "Veri Bilimi İçin Temel İstatistik",
        "author": "toygarpar",
        "intro": "Veri biliminde istatistiğin temel araçlarını öğrenin: Merkezi eğilim, dağılım, hipotez testi, regresyon ve daha fazlası.",
        "posts": dersler
    }, f, ensure_ascii=False, indent=4)