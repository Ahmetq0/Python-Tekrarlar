ürün1=float(input("Birinci ürünün fiyatini girinzi:\n"))
ürün2=float(input("İkinci ürünün fiyatini giriniz:\n"))

toplam=(float(ürün1)+float(ürün2))


if toplam<200:
    print("Ödemeniz gereken miktar:",toplam)
elif toplam>200:
    print("İndirimden sonra ödenecek miktar:",toplam /4)