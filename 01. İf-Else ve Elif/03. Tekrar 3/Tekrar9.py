
def hava_durumu_gir():
 hava=float(input("Hava durumunu giriniz:"))
 return (hava)

def hava_durumu_kontrol(hava):   
 if hava<5:
    print("Hava soğuk")
 elif hava >=6  ==14:
    print("Hava ılık")
 else:
    print("Hava Sıcak")


hava_değer = hava_durumu_gir()
hava_durumu_kontrol(hava_değer)