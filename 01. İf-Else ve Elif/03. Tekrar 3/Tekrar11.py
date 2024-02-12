
def kenar_uzunlukları_gir():
 kenar1=float(input("Birinci kenar değerini giriniz:"))
 kenar2=float(input("İkinci kenar değerini giriniz:"))
 kenar3=float(input("Üçüncü kenar değerini giriniz:"))
 return (kenar1,kenar2,kenar3)


def kenar_uzunlukları_kontrol_et(kenar1,kenar2,kenar3):
 if kenar1== kenar2== kenar3:
    print("Eşkenar üçgen")
 elif kenar1== kenar2:
    print("İkizkenar üçgen")
 else:
    print("Çeşitkenar üçgen")
    
kenar_değer = kenar_uzunlukları_gir()
kenar_uzunlukları_kontrol_et(kenar_değer[0],kenar_değer[1],kenar_değer[2])