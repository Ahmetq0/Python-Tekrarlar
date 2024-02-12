
def kenarı_gir():
 kenar1=float(input("Birinci değeri giriniz:\n"))
 kenar2=float(input("İkinci değeri giriniz:\n"))
 kenar3=float(input("Üçüncü değeri giriniz:\n"))
 return (kenar1,kenar2,kenar3)




def kenar_kontrol(kenar1,kenar2,kenar3):
 toplamdeğer=(float(kenar1)+float(kenar2)+float(kenar3))
 if toplamdeğer== 180:
    print("Bu bir üçgendir")
 else:
    print("Bu bir üçgen değildir")
    
kenar_değer = kenarı_gir()
kenar_kontrol(kenar_değer[0],kenar_değer[1],kenar_değer[2])