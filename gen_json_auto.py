import os

# posts klasöründeki .ipynb dosyalarını oku
dosyalar = sorted([f for f in os.listdir("posts") if f.endswith(".ipynb")])

# Sırayla yazdır
print("| No | Başlık | Açıklama |")
print("|----|--------|----------|")

for i, dosya in enumerate(dosyalar):
    # Dosya ismini temizle
    baslik = dosya.replace(".ipynb", "").replace("-", " ").title()
    
    print(f"| {i+1:02} | {baslik} | ... |")