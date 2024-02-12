
def sayı_girme():
 sayı=float(input("Sayıyı griniz:"))
 return (sayı)

def say_kontrol(sayı):
 if sayı %15 == 0:
    print("15e tam bölünür")
 else:
    print("15e tam bölünmez")
    

sayı_değer = sayı_girme()
say_kontrol(sayı_değer)