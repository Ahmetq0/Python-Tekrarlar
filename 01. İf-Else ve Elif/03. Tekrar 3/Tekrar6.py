def sayı_gir():
 sayı=float(input("Sayıyı giriniz:"))
 return (sayı)

def sayı_kontrol(sayı):
 if sayı %15 == 0:
    print("15e Tam bölünür")
 else:
    print("15e tam bölünmez")
    
sayı_değer = sayı_gir()
sayı_kontrol(sayı_değer)
    
