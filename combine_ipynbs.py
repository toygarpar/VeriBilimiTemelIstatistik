# tek tek pdf'ye çevir

# jupyter nbconvert "posts/01-istatiksel.ipynb" --to pdf







# Tüm posts/ klasöründeki notebook’ları ayrı ayrı PDF’e çevir:

# cd posts/
#for file in *.ipynb; do
#    jupyter nbconvert "$file" --to pdf
#done







# ilk adım latex install,  3 GB kadar yer tutuyor...

#sudo apt install texlive-latex-base texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra


#pdf kitap oluşturmak - tüm notebookları birleştirme




import nbformat
from nbformat.v4 import new_notebook

# Sıralı dosyaların listesi
notebook_files = [f"posts/{i:02d}-*.ipynb" for i in range(1, 28)]
notebook_files = [f"posts/{str(i).zfill(2)}-*.ipynb".replace('*','') for i in range(1, 28)]

# Yeni boş bir notebook oluştur
merged_nb = new_notebook()
merged_nb.cells = []

# Her notebook'u okuyup hücrelerini ekleyelim
for filename in notebook_files:
    try:
        with open(filename) as f:
            nb = nbformat.read(f, as_version=4)
            merged_nb.cells.extend(nb.cells)
    except FileNotFoundError:
        print(f"{filename} bulunamadı.")

# Birleşmiş notebook'u kaydet
with open("Temel_Istatistik_Kitap.ipynb", "w") as f:
    nbformat.write(merged_nb, f)

print("✅ Tüm notebook'lar birleştirildi: Temel_Istatistik_Kitap.ipynb")


# sonra bash'te 

# jupyter nbconvert "Temel_Istatistik_Kitap.ipynb" --to pdf --output "Temel_Istatistik_E-Kitap"

#özel bir latex şablonu için:

# jupyter nbconvert Temel_Istatistik_Kitap.ipynb --to pdf --template latex_template




