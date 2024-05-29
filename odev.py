import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def rastgele_koordinat_olustur():
    x = random.randint(0, 1000)
    y = random.randint(0, 1000)
    return x, y

def koordinatlari_kaydet(sayi, dosya_adı):
    koordinatlar = []
    for _ in range(sayi):
        x, y = rastgele_koordinat_olustur()
        koordinatlar.append((x, y))

    df = pd.DataFrame(koordinatlar, columns=['X Koordinatı', 'Y Koordinatı'])
    df.to_excel(dosya_adı, index=False)
    print(f"{sayi} adet koordinat excele kaydedildi.")

koordinatlari_kaydet(1000, "koordinatlar.xlsx")

# exceli okuyup dataframe'e dönüştür
def excel_den_koordinat_oku(excel_dosya):
    df = pd.read_excel(excel_dosya)
    return df

# Koordinatları ızgaralara bölen ve her bir ızgaradaki nokta grubunu farklı renk ile görselleştiren fonksiyon
def koordinatları_ızgaralara_bol_ve_gorsellestir(df, ızgaralar):
    plt.figure(figsize=(8, 6))
    for ızgara in ızgaralar:
        x_min, x_max, y_min, y_max = ızgara
        x_ızgara = df[(df['X Koordinatı'] >= x_min) & (df['X Koordinatı'] < x_max)]
        y_ızgara = x_ızgara[(x_ızgara['Y Koordinatı'] >= y_min) & (x_ızgara['Y Koordinatı'] < y_max)]
        plt.scatter(y_ızgara['X Koordinatı'], y_ızgara['Y Koordinatı'], alpha=0.5, label=f'{ızgara}', s=50)
 
    plt.title('Koordinatlar')
    plt.xlabel('X Koordinatı')
    plt.ylabel('Y Koordinatı')
    plt.grid(True)
    plt.show()

# excelden koordinatları oku
koordinat_df = excel_den_koordinat_oku("koordinatlar.xlsx")


# ızgaraları belirle
# 
grid_size = 200
x_ızgaralar = list(range(0, 1000, grid_size))
y_ızgaralar = list(range(0, 1000, grid_size))
ızgaralar = [(x, x + grid_size, y, y + grid_size) for x in x_ızgaralar for y in y_ızgaralar]
# koordinatları ızgaralara bölüp görselleştir
koordinatları_ızgaralara_bol_ve_gorsellestir(koordinat_df, ızgaralar)