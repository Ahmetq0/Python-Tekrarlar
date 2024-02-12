
def fiyat_gir():
 fiyat1=float(input("Birinci fiyatı giriniz:"))
 fiyat2=float(input("İkinci fiyatı giriniz:"))
 return (fiyat1,fiyat2)


def fiyat_kontrol(fiyat1,fiyat2): 
 toplam=(float(fiyat1)+float(fiyat2))
 if toplam<=200:
    
    print("Ödemeniz gereken ek ücret yok")
 elif toplam>=200:
    print("indirimden sonra ödemeniz gereken ücret",toplam/4)
    

fiyat_değer = fiyat_gir()
fiyat_kontrol(fiyat_değer[0],fiyat_değer[1])