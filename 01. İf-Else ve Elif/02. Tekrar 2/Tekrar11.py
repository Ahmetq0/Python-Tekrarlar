
def kenar_değer_gir():
 kenar1=float(input("Birinci kenar uzunluğunu giriniz:"))
 kenar2=float(input("İkinci kenar uzunluğunu giriniz:"))
 kenar3=float(input("Üçüncü kenar uzunluğunu giriniz:"))
 return (kenar1,kenar2,kenar3)


def kenar_kontrol(kenar1,kenar2,kenar3):
 if kenar1==kenar2==kenar3:
    print("Bu bir eşkenar üçgendir")
 elif kenar1==kenar2:
    print("Bu bir ikiz kenar üçgendir")
 else:
    print("Bu bir çeşit kenar üçgendir")
    

kenar_değer = kenar_değer_gir()
kenar_kontrol(kenar_değer[0],kenar_değer[1],kenar_değer[2])